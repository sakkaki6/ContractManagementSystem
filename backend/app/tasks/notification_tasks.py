from app.worker import celery
from app.db.session import SessionLocal


@celery.task
def send_notification(
    user_id: int,
    notification_type: str,
    title: str,
    message: str,
    contract_id: int = None,
):
    """
    Send a notification to a user
    """
    from app.models.notification import Notification, NotificationType

    db = SessionLocal()
    try:
        # Create notification
        notification = Notification(
            user_id=user_id,
            type=notification_type,
            title=title,
            message=message,
            contract_id=contract_id,
        )
        db.add(notification)
        db.commit()

        # TODO: Implement real-time notification via WebSockets
        # TODO: Implement email notification if configured

        return {"status": "success", "notification_id": notification.id}
    except Exception as e:
        db.rollback()
        return {"status": "error", "message": str(e)}
    finally:
        db.close()
