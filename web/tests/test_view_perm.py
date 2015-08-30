# -*- encoding: utf-8 -*-
import pytest

from django.core.urlresolvers import reverse

from base.tests.test_utils import PermTestCase
from block.models import Page
from block.tests.factories import PageFactory


class TestViewPerm(PermTestCase):

    def test_contact(self):
        PageFactory(
            slug=Page.CUSTOM,
            slug_menu='contact',
            template_name='compose/page_article.html',
            is_custom=True,
        )
        url = reverse('web.contact')
        self.assert_any(url)

    def test_home(self):
        PageFactory(
            is_home=True,
            slug='home',
            slug_menu='',
            template_name='compose/page_article.html',
        )
        url = reverse('project.home')
        self.assert_any(url)

    def test_login(self):
        url = reverse('login')
        self.assert_any(url)
