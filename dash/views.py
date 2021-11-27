# -*- encoding: utf-8 -*-
from django.views.generic import DetailView, ListView, TemplateView

from braces.views import LoginRequiredMixin, StaffuserRequiredMixin

from base.view_utils import BaseMixin, RedirectNextMixin
from contact.models import Contact
from contact.search import ContactIndex
from contact.views import ContactPermMixin
from crm.views import ContactTicketListMixin
from search.views import SearchViewMixin


class ContactDetailTicketListView(
    LoginRequiredMixin,
    ContactPermMixin,
    ContactTicketListMixin,
    RedirectNextMixin,
    BaseMixin,
    ListView,
):

    paginate_by = 20
    template_name = "dash/contact_detail.html"

    def test_contact(self):
        return self._contact()

class ContactReportDetailView(
    LoginRequiredMixin, StaffuserRequiredMixin, BaseMixin, DetailView
):
    model = Contact
    template_name = "dash/contact_report_detail.html"

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
