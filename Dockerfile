# Use Python 3.10 slim image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libsm6 \
    libxext6 \
    libxrender-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Django project
COPY . .

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=spatial_dashboard.settings

# Create necessary directories
RUN mkdir -p /app/spatial_dashboard/staticfiles /app/spatial_dashboard/media

# Run migrations without errors
RUN cd spatial_dashboard && python manage.py migrate --noinput --run-syncdb 2>/dev/null || true

# Expose port
EXPOSE 8000

# Run the Django server
CMD ["sh", "-c", "cd /app/spatial_dashboard && python manage.py runserver 0.0.0.0:8000"]