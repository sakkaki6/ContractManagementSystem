from datetime import datetime, timedelta
from app.worker import celery
from app.db.session import SessionLocal
from app.tasks.notification_tasks import send_notification


@celery.task
def check_expiring_contracts():
    """
    Check for contracts that are about to expire and send notifications
    """
    from app.models.contract import Contract, ContractStatus
    from app.models.user import User, UserRole

    db = SessionLocal()
    try:
        # Get current date
        today = datetime.now().date()

        # Find contracts that are about to expire in the next 30 days
        expiring_contracts = (
            db.query(Contract)
            .filter(
                Contract.status == ContractStatus.ACTIVE,
                Contract.expiration_date.between(today, today + timedelta(days=30)),
            )
            .all()
        )

        # Send notifications for each expiring contract
        for contract in expiring_contracts:
            # Calculate days until expiration
            days_until_expiration = (contract.expiration_date - today).days

            # Get contract owner
            owner = db.query(User).filter(User.id == contract.owner_id).first()

            # Get all users with manager role
            managers = db.query(User).filter(User.role == UserRole.MANAGER).all()

            # Notify contract owner
            if owner:
                send_notification.delay(
                    user_id=owner.id,
                    notification_type="CONTRACT_EXPIRING",
                    title=f"Contract Expiring Soon: {contract.title}",
                    message=f"Your contract '{contract.title}' will expire in {days_until_expiration} days.",
                    contract_id=contract.id,
                )

            # Notify managers
            for manager in managers:
                send_notification.delay(
                    user_id=manager.id,
                    notification_type="CONTRACT_EXPIRING",
                    title=f"Contract Expiring Soon: {contract.title}",
                    message=f"Contract '{contract.title}' will expire in {days_until_expiration} days.",
                    contract_id=contract.id,
                )

        return {"status": "success", "contracts_checked": len(expiring_contracts)}
    except Exception as e:
        return {"status": "error", "message": str(e)}
    finally:
        db.close()
