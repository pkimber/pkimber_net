# -*- encoding: utf-8 -*-
from django.urls import re_path

from .views import (
    ContactDetailTicketListView,
    ContactListView,
    ContactReportDetailView,
    HomeView,
    SearchView,
    SettingsView,
)


urlpatterns = [
    re_path(r"^contact/$", view=ContactListView.as_view(), name="contact.list"),
    re_path(
        r"^contact/(?P<pk>\d+)/$",
        view=ContactDetailTicketListView.as_view(),
        name="contact.detail",
    ),
    re_path(
        r"^contact/(?P<pk>\d+)/reports/$",
        view=ContactReportDetailView.as_view(),
        name="contact.report",
    ),
    re_path(r"^$", view=HomeView.as_view(), name="project.dash"),
    re_path(r"^search/$", view=SearchView.as_view(), name="project.search"),
    re_path(
        r"^settings/$",
        view=SettingsView.as_view(),
        name="project.settings",
    ),
]
