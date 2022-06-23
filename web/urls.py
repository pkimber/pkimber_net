# -*- encoding: utf-8 -*-
from django.urls import re_path

from block.models import Page
from .views import CmsHomePageView, EnquiryCreateView


urlpatterns = [
    # home
    re_path(
        r"^$",
        view=CmsHomePageView.as_view(),
        kwargs=dict(page=Page.HOME),
        name="project.home",
    ),
    # contact form
    re_path(
        r"^contact/$",
        view=EnquiryCreateView.as_view(),
        kwargs=dict(page=Page.CUSTOM, menu="contact"),
        name="web.contact",
    ),
]
