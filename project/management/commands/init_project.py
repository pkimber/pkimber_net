"""
This command is designed to be run multiple times.  It will clear out data, and
then re-insert e.g. for setting up the main menu navigation.
"""
from django.core.management.base import BaseCommand

from web.tests.scenario import init_app_web


class Command(BaseCommand):

    help = "Set-up project (e.g. main navigation)"

    def handle(self, *args, **options):
        init_app_web()
        print("Project initialised...")
