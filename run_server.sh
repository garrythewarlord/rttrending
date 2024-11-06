# Start the Django development server
gunicorn rttrending.wsgi:application &

# Start Celery worker
celery -A rttrending worker --loglevel=DEBUG &

# Start Celery beat
celery -A rttrending beat --loglevel=DEBUG &

# Wait for all background processes to complete
wait