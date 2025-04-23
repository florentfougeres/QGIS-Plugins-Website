from __future__ import absolute_import

import os

from celery import Celery
import logging

logger = logging.getLogger('plugins')


app = Celery("plugins")

app.autodiscover_tasks(["plugins.tasks"])
