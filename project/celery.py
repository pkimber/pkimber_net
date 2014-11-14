# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from celery import Celery

from django.conf import settings

app = Celery('project')
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
