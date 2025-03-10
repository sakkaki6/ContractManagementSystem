# Import all the models, so that Base has them before being imported by Alembic
from app.db.session import Base
from app.models.user import User
from app.models.contract import Contract
from app.models.approval import Approval
from app.models.notification import Notification
from app.models.comment import Comment
from app.models.audit_log import AuditLog
