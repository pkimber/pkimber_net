# -*- encoding: utf-8 -*-
from braces.views import LoginRequiredMixin, StaffuserRequiredMixin
from django.views.generic import DetailView, ListView, TemplateView

from base.view_utils import BaseMixin, RedirectNextMixin
from contact.search import ContactIndex
from contact.views import ContactPermMixin, ContactListMixin
from crm.views import ContactTicketListMixin
from invoice.views import InvoiceListMixin
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


class ContactListView(
    LoginRequiredMixin,
    StaffuserRequiredMixin,
    ContactListMixin,
    BaseMixin,
    ListView,
):
    template_name = "dash/contact_list.html"


class HomeView(
    LoginRequiredMixin, StaffuserRequiredMixin, BaseMixin, TemplateView
):
    template_name = "dash/home.html"


class InvoiceListView(
    LoginRequiredMixin,
    StaffuserRequiredMixin,
    InvoiceListMixin,
    BaseMixin,
    ListView,
):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({"show_download": True})
        return context


class SearchView(LoginRequiredMixin, StaffuserRequiredMixin, SearchViewMixin):
    INDEX_CHOICES = (("contact", "Contact"),)
    INDEX_CLASSES = {"contact": ContactIndex}


class SettingsView(
    LoginRequiredMixin, StaffuserRequiredMixin, BaseMixin, TemplateView
):
    template_name = "dash/settings.html"
