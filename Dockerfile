# This Dockerfile is used to deploy a single-container Reflex app instance.
FROM python:3.11

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PATH="/app/.venv/bin:$PATH"

# Set the working directory
WORKDIR /app

# Install app dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application files
COPY . .

# Ensure the necessary directories exist
RUN mkdir -p /app/.local/share/reflex

# Initialize the application
RUN reflex init

# Build the frontend only
RUN reflex export --frontend-only --no-zip

# Ensure correct permissions for the application directory
RUN chown -R root:root /app

# Expose necessary ports
EXPOSE 8000 3000

# Run the backend only
CMD [ -d alembic ] && reflex db migrate; reflex run --backend-only
