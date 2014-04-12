# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.core.urlresolvers import reverse

from base.tests.test_utils import PermTestCase
from block.tests.scenario import init_app_block

from web.tests.scenario import init_app_web


class TestViewPerm(PermTestCase):

    def setUp(self):
        init_app_block()
        init_app_web()

    def _project_page_url(self, page):
        return reverse(
            'project.page',
            kwargs=dict(page=page,)
        )

    def test_contact(self):
        url = self._project_page_url('contact')
        self.assert_any(url)

    def test_home(self):
        url = reverse('project.home')
        self.assert_any(url)

    def test_home_block(self):
        url = self._project_page_url('home')
        self.assert_any(url)

    def test_login(self):
        url = reverse('login')
        self.assert_any(url)

    def test_portfolio(self):
        url = self._project_page_url('portfolio')
        self.assert_any(url)

    def test_technology(self):
        url = self._project_page_url('technology')
        self.assert_any(url)
