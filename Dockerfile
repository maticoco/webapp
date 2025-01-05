# Dockerfile for Reflex Simple-Two-Port

# Base image
FROM python:3.11

# Install Redis and required dependencies
RUN apt-get update && apt-get install -y redis-server && rm -rf /var/lib/apt/lists/*
ENV REDIS_URL=redis://localhost PYTHONUNBUFFERED=1

# Copy application files
WORKDIR /app
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Initialize Reflex and prepare app
RUN reflex init

# Build frontend
RUN reflex export --frontend-only --no-zip

# Handle signals properly
STOPSIGNAL SIGKILL

# Apply migrations and start servers
CMD [ -d alembic ] && reflex db migrate; \
    redis-server --daemonize yes && \
    exec reflex run --env prod