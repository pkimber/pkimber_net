# -*- encoding: utf-8 -*-
from django.core.management.base import BaseCommand
from pytz import utc

from base.scheduler_utils import create_scheduler


class Command(BaseCommand):
    """Start APScheduler scheduler."""

    help = "Start APScheduler..."

    def handle(self, *args, **options):
        self.stdout.write("{}...".format(self.help))
        scheduler = create_scheduler()
        self.stdout.write("Scheduler, adding jobs...")
        # rebuild_contact_index
        scheduler.add_job(
            "contact.tasks:schedule_rebuild_contact_index",
            "cron",
            hour=1,
            minute=10,
            id="schedule_rebuild_contact_index",
            max_instances=1,
            replace_existing=True,
        )
        # rebuild_ticket_index
        scheduler.add_job(
            "crm.tasks:schedule_rebuild_ticket_index",
            "cron",
            hour=1,
            minute=30,
            id="schedule_rebuild_ticket_index",
            max_instances=1,
            replace_existing=True,
        )
        # process_mail
        scheduler.add_job(
            "mail.tasks:schedule_process_mail",
            "interval",
            minutes=60,
            id="schedule_process_mail",
            max_instances=1,
            replace_existing=True,
        )
        self.stdout.write("Scheduler, starting...")
        scheduler.start()
        self.stdout.write("{} - Complete".format(self.help))
