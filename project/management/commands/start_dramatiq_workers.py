# -*- encoding: utf-8 -*-
from django.conf import settings

from base.dramatiq_utils import DramatiqBaseCommandMixin


class Command(DramatiqBaseCommandMixin):
    """Start Dramatiq workers - using the correct queue name."""

    PROCESSES = 3

    def get_queue_name(self):
        return settings.DRAMATIQ_QUEUE_NAME
