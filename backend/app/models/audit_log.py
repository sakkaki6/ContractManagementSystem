from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, Enum, Text, JSON
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import enum

from app.db.session import Base


class AuditActionType(str, enum.Enum):
    CREATE = "create"
    UPDATE = "update"
    DELETE = "delete"
    VIEW = "view"
    APPROVE = "approve"
    REJECT = "reject"
    DOWNLOAD = "download"
    EXPORT = "export"
    LOGIN = "login"
    LOGOUT = "logout"


class AuditLog(Base):
    __tablename__ = "audit_logs"

    id = Column(Integer, primary_key=True, index=True)
    action = Column(Enum(AuditActionType), nullable=False)
    entity_type = Column(String, nullable=False)  # e.g., "contract", "user", "approval"
    entity_id = Column(Integer)
    description = Column(Text)
    ip_address = Column(String)
    user_agent = Column(String)
    changes = Column(JSON)  # Store changes in JSON format

    # Foreign keys
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    contract_id = Column(Integer, ForeignKey("contracts.id"), nullable=True)

    # Timestamps
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # Relationships
    contract = relationship("Contract", back_populates="audit_logs")

    def __repr__(self):
        return f"<AuditLog {self.id} - {self.action} {self.entity_type}>"
