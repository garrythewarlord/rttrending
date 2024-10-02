import os
from celery import Celery
from django.conf import settings  # Make sure this line is included

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rttrending.settings')  # Adjust this to your project

app = Celery('rttrending')

# Using the namespace='CELERY' option to read configuration from Django settings
app.config_from_object('django.conf:settings', namespace='CELERY')

# Auto-discover tasks from all registered Django apps
app.autodiscover_tasks()