# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import (
    patterns,
    url,
)
from django.contrib import admin

from block.views import (
    PageDesignView,
    PageView,
)

from .views import (
    MainCreateView,
    MainPublishView,
    MainRemoveView,
    MainUpdateView,
)


from .models import PAGE_HOME


admin.autodiscover()


urlpatterns = patterns(
    '',
    # Main
    url(regex=r'^main/create/(?P<page>[-\w\d]+)/(?P<section>[-\w\d]+)/$',
        view=MainCreateView.as_view(),
        name='web.main.create'
        ),
    url(regex=r'^main/(?P<pk>\d+)/publish/$',
        view=MainPublishView.as_view(),
        name='web.main.publish'
        ),
    url(regex=r'^main/(?P<pk>\d+)/remove/$',
        view=MainRemoveView.as_view(),
        name='web.main.remove'
        ),
    url(regex=r'^main/(?P<pk>\d+)/edit/$',
        view=MainUpdateView.as_view(),
        name='web.main.update'
        ),
    # pages using the 'block' app
    url(regex=r'^$',
        view=PageView.as_view(),
        kwargs=dict(page=PAGE_HOME),
        name='project.home'
        ),
    url(regex=r'^(?P<page>[-\w\d]+)/design/$',
        view=PageDesignView.as_view(),
        name='project.page.design'
        ),
    url(regex=r'^(?P<page>[-\w\d]+)/$',
        view=PageView.as_view(),
        name='project.page'
        ),
)
