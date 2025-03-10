import sys
from pathlib import Path

# Add the parent directory to the path so we can import our app
sys.path.append(str(Path(__file__).parent.parent))

from app.db.base import Base
from app.core.config import settings

# This is the Alembic Config object, which provides access to the values within the .ini file
config = context.config

# Override sqlalchemy.url with the value from settings
config.set_main_option("sqlalchemy.url", str(settings.DATABASE_URI))

# Interpret the config file for Python logging
fileConfig(config.config_file_name)

# Add your model's MetaData object here for 'autogenerate' support
target_metadata = Base.metadata
