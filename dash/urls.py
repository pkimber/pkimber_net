# -*- encoding: utf-8 -*-
from django.conf.urls import url

from .views import ContactDetailView, HomeView, SettingsView


urlpatterns = [
    url(regex=r'^contact/(?P<slug>[-\w\d]+)/$',
        view=ContactDetailView.as_view(),
        name='contact.detail'
        ),
    url(regex=r'^$',
        view=HomeView.as_view(),
        name='project.dash'
        ),
    url(regex=r'^settings/$',
        view=SettingsView.as_view(),
        name='project.settings'
        ),
]
