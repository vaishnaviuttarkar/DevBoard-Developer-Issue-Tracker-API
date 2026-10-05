import os
from celery import Celery

# celery needs access to django settings
os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "config.settings"
)

# celery application is created
app = Celery("devboard")

# Load django settings: 
# this tells celery to read celery configuration django's settings.py
os.config_from_object(
    "django.conf:settings",
    namespace = "CELERY"
) #The namespace="CELERY" means settings will look like: CELERY_BROKER_URL

app.autodiscover_tasks()