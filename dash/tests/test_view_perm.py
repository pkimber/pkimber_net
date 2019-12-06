# -*- encoding: utf-8 -*-
import pytest

from django.urls import reverse
from http import HTTPStatus

from contact.tests.factories import ContactFactory, UserContactFactory
from login.tests.factories import TEST_PASSWORD, UserFactory
from login.tests.fixture import perm_check
from login.tests.scenario import get_user_web


@pytest.mark.django_db
def test_contact_detail(perm_check):
    UserContactFactory(user=get_user_web())
    user_contact = UserContactFactory()
    url = reverse("contact.detail", args=[user_contact.contact.pk])
    perm_check.staff(url)


@pytest.mark.django_db
def test_contact_detail_for_user(client):
    user = UserFactory(is_staff=False)
    contact = ContactFactory(user=user)
    assert client.login(username=user.username, password=TEST_PASSWORD) is True
    response = client.get(reverse("contact.detail", args=[contact.pk]))
    assert HTTPStatus.OK == response.status_code


@pytest.mark.django_db
def test_contact_list(perm_check):
    url = reverse("contact.list")
    perm_check.staff(url)


@pytest.mark.django_db
def test_dash(perm_check):
    url = reverse("project.dash")
    perm_check.staff(url)


@pytest.mark.django_db
def test_search(perm_check):
    url = reverse("project.search")
    perm_check.staff(url)


@pytest.mark.django_db
def test_invoice_list(perm_check):
    url = reverse("invoice.list")
    perm_check.staff(url)


@pytest.mark.django_db
def test_settings(perm_check):
    url = reverse("project.settings")
    perm_check.staff(url)
