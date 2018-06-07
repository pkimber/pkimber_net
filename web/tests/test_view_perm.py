# -*- encoding: utf-8 -*-
import pytest

from django.urls import reverse

from base.tests.test_utils import PermTestCase
from block.models import Page
from block.tests.factories import PageFactory, TemplateFactory
from enquiry.models import Enquiry
from gdpr.tests.factories import ConsentFactory


class TestViewPerm(PermTestCase):

    def test_contact(self):

        ConsentFactory(slug=Enquiry.GDPR_CONTACT_SLUG)
        PageFactory(
            slug=Page.CUSTOM,
            slug_menu="contact",
            template=TemplateFactory(template_name="compose/page_article.html"),
            is_custom=True,
        )
        url = reverse("web.contact")
        self.assert_any(url)

    def test_home(self):
        PageFactory(
            is_home=True,
            slug="home",
            slug_menu="",
            template=TemplateFactory(template_name="compose/page_article.html"),
        )
        url = reverse("project.home")
        self.assert_any(url)

    def test_login(self):
        url = reverse("login")
        self.assert_any(url)
