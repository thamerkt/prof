#!/bin/sh

# Wait for the database to be ready
echo "⏳ Waiting for DB to be ready..."
until python manage.py dbshell < /dev/null; do
  echo "DB is unavailable - sleeping"
  sleep 2
done

echo "🚀 Running migrations..."
python manage.py migrate --noinput

echo "📦 Starting Django server..."
python manage.py runserver 0.0.0.0:8000
