"""
This command is designed to be run multiple times.  It will clear out data, and
then re-insert e.g. for setting up the main menu navigation.
"""
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    help = "Set-up project (e.g. main navigation)"

    def handle(self, *args, **options):
        print("Project initialised...")
