# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

from block.management.commands import init_app_block

# from login.management.commands import demo_data_login
# from member.management.commands import demo_data_member
# from web.management.commands import demo_data_web

from project.management.commands import init_project


class TestManagementCommand(TestCase):

    def test_init_project(self):
        """Test the management command."""
        pre_command = init_app_block.Command()
        pre_command.handle()

        # pre_command = demo_data_login.Command()
        # pre_command.handle()
        # pre_command = demo_data_member.Command()
        # pre_command.handle()
        # pre_command = demo_data_web.Command()
        # pre_command.handle()
        # We are testing this command!
        command = init_project.Command()
        command.handle()
