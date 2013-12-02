from django.conf import settings
from django.conf.urls import include
from django.conf.urls import patterns
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin

from .views import (
    ContactView,
    HomeView,
    PortfolioView,
    TechnologyView,
    TempView,
)


admin.autodiscover()


urlpatterns = patterns(
    '',
    url(regex=r'^$',
        view=HomeView.as_view(),
        name='project.home'
        ),
    url(regex=r'^me/contact/$',
        view=ContactView.as_view(),
        name='project.contact'
        ),
    url(regex=r'^me/portfolio/$',
        view=PortfolioView.as_view(),
        name='project.portfolio'
        ),
    url(regex=r'^me/technology/$',
        view=TechnologyView.as_view(),
        name='project.technology'
        ),
    url(regex=r'^temp/$',
        view=TempView.as_view(),
        name='project.temp'
        ),
    url(regex=r'^',
        view=include('login.urls')
        ),
    url(regex=r'^admin/',
        view=include(admin.site.urls)
        ),
    url(regex=r'^crm/',
        view=include('crm.urls')
        ),
    url(regex=r'^invoice/',
        view=include('invoice.urls')
        ),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#   ^ helper function to return a URL pattern for serving files in debug mode.
# https://docs.djangoproject.com/en/1.5/howto/static-files/#serving-files-uploaded-by-a-user
