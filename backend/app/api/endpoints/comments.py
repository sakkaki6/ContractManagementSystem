from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.comment import Comment

router = APIRouter()


@router.get("/", response_model=List[dict])
async def read_comments(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    """
    Retrieve comments.
    """
    comments = db.query(Comment).offset(skip).limit(limit).all()
    return [
        {
            "id": comment.id,
            "content": comment.content,
            "user_id": comment.user_id,
            "contract_id": comment.contract_id,
            "parent_id": comment.parent_id,
            "created_at": comment.created_at,
            "updated_at": comment.updated_at,
        }
        for comment in comments
    ]


@router.get("/{comment_id}", response_model=dict)
async def read_comment(
    comment_id: int,
    db: Session = Depends(get_db),
) -> Any:
    """
    Get a specific comment by id.
    """
    comment = db.query(Comment).filter(Comment.id == comment_id).first()
    if not comment:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Comment not found",
        )
    return {
        "id": comment.id,
        "content": comment.content,
        "user_id": comment.user_id,
        "contract_id": comment.contract_id,
        "parent_id": comment.parent_id,
        "created_at": comment.created_at,
        "updated_at": comment.updated_at,
    }
