import os
from celery import Celery

# set default Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Celery_report_genarator.settings')

app = Celery('Celery_report_genarator')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Auto-discover tasks from all installed apps
app.autodiscover_tasks()