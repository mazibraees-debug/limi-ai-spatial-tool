#!/bin/bash
cd /app/spatial_dashboard

# Run migrations at startup
python manage.py migrate --noinput --run-syncdb 2>/dev/null || true

# Start the Django server
python manage.py runserver 0.0.0.0:8000
