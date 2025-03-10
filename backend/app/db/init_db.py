import logging
from sqlalchemy.orm import Session

from app.db.session import SessionLocal
from app.core.config import settings
from app.models.user import User, UserRole
from app.utils.security import get_password_hash


logger = logging.getLogger(__name__)


async def init_db() -> None:
    db = SessionLocal()
    try:
        # Check if we already have users
        user = db.query(User).filter(User.email == settings.FIRST_SUPERUSER).first()
        if not user:
            logger.info("Creating initial superuser")

            # Create superuser
            user_in = User(
                email=settings.FIRST_SUPERUSER,
                hashed_password=get_password_hash(settings.FIRST_SUPERUSER_PASSWORD),
                first_name="Admin",
                last_name="User",
                role=UserRole.ADMIN,
                is_active=True,
                is_superuser=True,
            )
            db.add(user_in)
            db.commit()
            logger.info(f"Superuser {settings.FIRST_SUPERUSER} created")
        else:
            logger.info("Superuser already exists in database")
    except Exception as e:
        logger.error(f"Error creating superuser: {e}")
    finally:
        db.close()
