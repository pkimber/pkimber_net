# -*- encoding: utf-8 -*-
from django.conf.urls import (
    patterns,
    url,
)

from block.models import Page
from .views import (
    CmsHomePageView,
    EnquiryCreateView,
)


urlpatterns = patterns(
    '',
    # home
    url(regex=r'^$',
        view=CmsHomePageView.as_view(),
        kwargs=dict(page=Page.HOME),
        name='project.home'
        ),
    # contact form
    url(regex=r'^contact/$',
        view=EnquiryCreateView.as_view(),
        kwargs=dict(page=Page.CUSTOM, menu='contact'),
        name='web.contact'
        ),
)
