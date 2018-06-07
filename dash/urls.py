# -*- encoding: utf-8 -*-
from django.conf.urls import url

from .views import ContactDetailView, HomeView, SearchView, SettingsView


urlpatterns = [
    url(
        regex=r"^contact/(?P<pk>\d+)/$",
        view=ContactDetailView.as_view(),
        name="contact.detail",
    ),
    url(regex=r"^$", view=HomeView.as_view(), name="project.dash"),
    url(regex=r"^search/$", view=SearchView.as_view(), name="project.search"),
    url(
        regex=r"^settings/$",
        view=SettingsView.as_view(),
        name="project.settings",
    ),
]
