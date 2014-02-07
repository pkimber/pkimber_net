"""
This command is designed to be run multiple times.  It will clear out data, and
then re-insert e.g. for setting up the main menu navigation.
"""
from django.core.management.base import BaseCommand

from cms.service import (
    init_layout,
    init_page,
    init_section,
)
from cms.tests.scenario import default_moderate_state


class Command(BaseCommand):

    help = "Set-up project (e.g. main navigation)"

    def handle(self, *args, **options):
        default_moderate_state()
        # pages
        home = init_page('Home', 0, is_home=True)
        portfolio = init_page('Portfolio', 1)
        tech = init_page('Tech', 2)
        # layout
        body = init_layout('Body')
        # sections
        init_section(home, body)
        init_section(portfolio, body)
        init_section(tech, body)
        print("Project initialised...")
