# -*- encoding: utf-8 -*-
"""
This command is designed to be run multiple times.  It will clear out data, and
then re-insert e.g. for setting up the main menu navigation.
"""
from django.core.management.base import BaseCommand

from block.models import Page


class Command(BaseCommand):

    help = "Set-up project (e.g. main navigation)"

    def handle(self, *args, **options):
        self.stdout.write('Pages - Contact')
        Page.objects.init_page(
            Page.CUSTOM,
            'contact',
            'Contact',
            1,
            'compose/page_article.html',
            is_custom=True,
        )
        Page.objects.init_page(
            'contact',
            'thankyou',
            'Thank You',
            0,
            'compose/page_article.html',
        )
        print("Project initialised...")
