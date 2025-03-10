#!/bin/bash

set -e

# Wait for PostgreSQL to be ready
echo "Waiting for PostgreSQL..."
while ! nc -z $POSTGRES_SERVER $POSTGRES_PORT; do
  sleep 0.1
done
echo "PostgreSQL started"

# Wait for Redis to be ready
echo "Waiting for Redis..."
while ! nc -z $REDIS_HOST $REDIS_PORT; do
  sleep 0.1
done
echo "Redis started"

# Apply database migrations
echo "Applying database migrations..."
alembic upgrade head

# Create initial superuser if needed
python -c "
import asyncio
from app.db.init_db import init_db
asyncio.run(init_db())
"

exec "$@" 