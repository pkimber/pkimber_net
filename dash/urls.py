# -*- encoding: utf-8 -*-
from django.conf.urls import url

from .views import (
    ContactDetailTicketListView,
    ContactListView,
    HomeView,
    InvoiceListView,
    SearchView,
    SettingsView,
)


urlpatterns = [
    url(regex=r"^$", view=HomeView.as_view(), name="project.dash"),
    url(
        regex=r"^contact/(?P<pk>\d+)/$",
        view=ContactDetailTicketListView.as_view(),
        name="contact.detail",
    ),
    url(
        regex=r"^contact/$", view=ContactListView.as_view(), name="contact.list"
    ),
    url(
        regex=r"^invoice/$", view=InvoiceListView.as_view(), name="invoice.list"
    ),
    url(regex=r"^search/$", view=SearchView.as_view(), name="project.search"),
    url(
        regex=r"^settings/$",
        view=SettingsView.as_view(),
        name="project.settings",
    ),
]
