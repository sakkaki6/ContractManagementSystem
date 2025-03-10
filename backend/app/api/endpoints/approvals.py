from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.approval import Approval

router = APIRouter()


@router.get("/", response_model=List[dict])
async def read_approvals(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    """
    Retrieve approvals.
    """
    approvals = db.query(Approval).offset(skip).limit(limit).all()
    return [
        {
            "id": approval.id,
            "status": approval.status,
            "comments": approval.comments,
            "step_order": approval.step_order,
            "contract_id": approval.contract_id,
            "approver_id": approval.approver_id,
            "created_at": approval.created_at,
            "updated_at": approval.updated_at,
            "approved_at": approval.approved_at,
        }
        for approval in approvals
    ]


@router.get("/{approval_id}", response_model=dict)
async def read_approval(
    approval_id: int,
    db: Session = Depends(get_db),
) -> Any:
    """
    Get a specific approval by id.
    """
    approval = db.query(Approval).filter(Approval.id == approval_id).first()
    if not approval:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Approval not found",
        )
    return {
        "id": approval.id,
        "status": approval.status,
        "comments": approval.comments,
        "step_order": approval.step_order,
        "contract_id": approval.contract_id,
        "approver_id": approval.approver_id,
        "created_at": approval.created_at,
        "updated_at": approval.updated_at,
        "approved_at": approval.approved_at,
    }
