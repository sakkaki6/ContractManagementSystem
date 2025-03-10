from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.notification import Notification

router = APIRouter()


@router.get("/", response_model=List[dict])
async def read_notifications(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    """
    Retrieve notifications.
    """
    notifications = db.query(Notification).offset(skip).limit(limit).all()
    return [
        {
            "id": notification.id,
            "type": notification.type,
            "title": notification.title,
            "message": notification.message,
            "is_read": notification.is_read,
            "user_id": notification.user_id,
            "contract_id": notification.contract_id,
            "created_at": notification.created_at,
            "read_at": notification.read_at,
        }
        for notification in notifications
    ]


@router.get("/{notification_id}", response_model=dict)
async def read_notification(
    notification_id: int,
    db: Session = Depends(get_db),
) -> Any:
    """
    Get a specific notification by id.
    """
    notification = (
        db.query(Notification).filter(Notification.id == notification_id).first()
    )
    if not notification:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Notification not found",
        )
    return {
        "id": notification.id,
        "type": notification.type,
        "title": notification.title,
        "message": notification.message,
        "is_read": notification.is_read,
        "user_id": notification.user_id,
        "contract_id": notification.contract_id,
        "created_at": notification.created_at,
        "read_at": notification.read_at,
    }
