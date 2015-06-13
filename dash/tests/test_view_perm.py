# -*- encoding: utf-8 -*-
from django.core.urlresolvers import reverse

from base.tests.test_utils import PermTestCase


class TestViewPerm(PermTestCase):

    def setUp(self):
        self.setup_users()

    def test_dash(self):
        self.assert_staff_only(reverse('project.dash'))

    def test_settings(self):
        self.assert_staff_only(reverse('project.settings'))
