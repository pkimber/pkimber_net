# -*- encoding: utf-8 -*-
from django.views.generic import DetailView, TemplateView

from braces.views import LoginRequiredMixin, StaffuserRequiredMixin

from base.view_utils import BaseMixin
from contact.search import ContactIndex
from crm.views import CrmContactDetailMixin
from search.views import SearchViewMixin


class ContactDetailView(
    LoginRequiredMixin, CrmContactDetailMixin, BaseMixin, DetailView
):
    pass


class HomeView(
    LoginRequiredMixin, StaffuserRequiredMixin, BaseMixin, TemplateView
):

    template_name = "dash/home.html"


class SearchView(LoginRequiredMixin, StaffuserRequiredMixin, SearchViewMixin):

    INDEX_CHOICES = (("contact", "Contact"),)

    INDEX_CLASSES = {"contact": ContactIndex}


class SettingsView(
    LoginRequiredMixin, StaffuserRequiredMixin, BaseMixin, TemplateView
):

    template_name = "dash/settings.html"
