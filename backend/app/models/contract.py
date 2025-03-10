from sqlalchemy import (
    Boolean,
    Column,
    String,
    Integer,
    DateTime,
    ForeignKey,
    Enum,
    Text,
    Date,
    Float,
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import enum

from app.db.session import Base


class ContractStatus(str, enum.Enum):
    DRAFT = "draft"
    PENDING_APPROVAL = "pending_approval"
    APPROVED = "approved"
    ACTIVE = "active"
    EXPIRED = "expired"
    TERMINATED = "terminated"
    ARCHIVED = "archived"


class ContractType(str, enum.Enum):
    SERVICE = "service"
    PRODUCT = "product"
    EMPLOYMENT = "employment"
    LEASE = "lease"
    LICENSE = "license"
    NDA = "nda"
    OTHER = "other"


class Contract(Base):
    __tablename__ = "contracts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(Text)
    contract_type = Column(Enum(ContractType), default=ContractType.SERVICE)
    status = Column(Enum(ContractStatus), default=ContractStatus.DRAFT)
    content = Column(Text)
    version = Column(Integer, default=1)
    reference_number = Column(String, unique=True, index=True)
    effective_date = Column(Date)
    expiration_date = Column(Date)
    value = Column(Float)
    currency = Column(String, default="USD")
    auto_renewal = Column(Boolean, default=False)
    renewal_reminder_days = Column(Integer, default=30)
    file_path = Column(String)

    # Foreign keys
    owner_id = Column(Integer, ForeignKey("users.id"))

    # Timestamps
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # Relationships
    owner = relationship("User", back_populates="contracts")
    approvals = relationship("Approval", back_populates="contract")
    comments = relationship("Comment", back_populates="contract")
    audit_logs = relationship("AuditLog", back_populates="contract")

    def __repr__(self):
        return f"<Contract {self.title}>"
