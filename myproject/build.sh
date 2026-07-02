#!/usr/bin/env bash
# Exit on error
set -o errexit

echo "📦 Installing Python dependencies..."
pip install -r requirements.txt

echo "🎨 Collecting static files for WhiteNoise..."
python manage.py collectstatic --no-input

echo "✅ Build completed successfully!"
