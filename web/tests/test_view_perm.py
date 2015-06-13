# -*- encoding: utf-8 -*-
import pytest

from django.core.urlresolvers import reverse

from base.tests.test_utils import PermTestCase
from block.models import BlockError
from web.tests.scenario import init_app_web


class TestViewPerm(PermTestCase):

    def setUp(self):
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
        """Check the URL for the block ('/home/') raises an exception."""
        url = self._project_page_url('home')
        with pytest.raises(BlockError) as e:
            self.assert_any(url)
        assert 'does not match the absolute url' in str(e.value)

    def test_login(self):
        url = reverse('login')
        self.assert_any(url)

    def test_portfolio(self):
        url = self._project_page_url('portfolio')
        self.assert_any(url)

    def test_technology(self):
        url = self._project_page_url('technology')
        self.assert_any(url)
