# -*- encoding: utf-8 -*-
import pytest

from django.urls import reverse

from contact.tests.factories import UserContactFactory
from login.tests.fixture import perm_check
from login.tests.scenario import get_user_web


@pytest.mark.django_db
def test_contact_detail(perm_check):
    UserContactFactory(user=get_user_web())
    user_contact = UserContactFactory()
    url = reverse('contact.detail', args=[user_contact.contact.pk])
    perm_check.staff(url)


@pytest.mark.django_db
def test_dash(perm_check):
    url = reverse('project.dash')
    perm_check.staff(url)


@pytest.mark.django_db
def test_search(perm_check):
    url = reverse('project.search')
    perm_check.staff(url)


@pytest.mark.django_db
def test_settings(perm_check):
    url = reverse('project.settings')
    perm_check.staff(url)
