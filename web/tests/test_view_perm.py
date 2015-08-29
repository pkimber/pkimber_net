# -*- encoding: utf-8 -*-
import pytest

from django.core.urlresolvers import reverse

from base.tests.test_utils import PermTestCase


class TestViewPerm(PermTestCase):

    def test_home(self):
        url = reverse('project.home')
        self.assert_any(url)

    def test_login(self):
        url = reverse('login')
        self.assert_any(url)
