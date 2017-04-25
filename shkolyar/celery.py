from __future__ import absolute_import
import os

from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shkolyar.settings')
app = Celery('shkolyar')

# используем установки django-проекта в celery-приложении
app.config_from_object('django.conf:settings')

# автоопределение задач из django-проекта
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

