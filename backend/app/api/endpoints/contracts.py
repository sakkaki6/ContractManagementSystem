from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.contract import Contract

router = APIRouter()


@router.get("/", response_model=List[dict])
async def read_contracts(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    """
    Retrieve contracts.
    """
    contracts = db.query(Contract).offset(skip).limit(limit).all()
    return [
        {
            "id": contract.id,
            "title": contract.title,
            "description": contract.description,
            "contract_type": contract.contract_type,
            "status": contract.status,
            "reference_number": contract.reference_number,
            "effective_date": contract.effective_date,
            "expiration_date": contract.expiration_date,
            "value": contract.value,
            "currency": contract.currency,
            "owner_id": contract.owner_id,
            "created_at": contract.created_at,
            "updated_at": contract.updated_at,
        }
        for contract in contracts
    ]


@router.get("/{contract_id}", response_model=dict)
async def read_contract(
    contract_id: int,
    db: Session = Depends(get_db),
) -> Any:
    """
    Get a specific contract by id.
    """
    contract = db.query(Contract).filter(Contract.id == contract_id).first()
    if not contract:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Contract not found",
        )
    return {
        "id": contract.id,
        "title": contract.title,
        "description": contract.description,
        "contract_type": contract.contract_type,
        "status": contract.status,
        "content": contract.content,
        "version": contract.version,
        "reference_number": contract.reference_number,
        "effective_date": contract.effective_date,
        "expiration_date": contract.expiration_date,
        "value": contract.value,
        "currency": contract.currency,
        "auto_renewal": contract.auto_renewal,
        "renewal_reminder_days": contract.renewal_reminder_days,
        "file_path": contract.file_path,
        "owner_id": contract.owner_id,
        "created_at": contract.created_at,
        "updated_at": contract.updated_at,
    }
