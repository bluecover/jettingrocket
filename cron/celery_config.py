# coding: utf-8

BROKER_URL = 'redis://localhost:6379/11'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/12'
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT = ['json']
CELERYD_CONCURRENCY = 1
CELERY_ENABLE_UTC = False  # Use system local timezone.

# CELERY_TIMEZONE = 'Europe/Oslo'
