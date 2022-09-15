# -*- encoding: utf-8 -*-
from django.conf import settings
from django.urls import include, re_path
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap
from django.urls import path
from rest_framework.authtoken import views

from block.models import Page


info_dict = {"queryset": Page.objects.pages(), "date_field": "modified"}

sitemaps = {
    "block": GenericSitemap(info_dict, priority=0.5, changefreq="monthly")
}


urlpatterns = [
    re_path(r"^", view=include("login.urls")),
    re_path(r"^api/0.1/", view=include("crm.urls_api")),
    re_path(r"^block/", view=include("block.urls.block")),
    re_path(r"^compose/", view=include("compose.urls.compose")),
    re_path(r"^contact/", view=include("contact.urls")),
    re_path(r"^crm/", view=include("crm.urls")),
    re_path(r"^dash/", view=include("dash.urls")),
    re_path(r"^enquiry/", view=include("enquiry.urls")),
    re_path(r"^gdpr/", view=include("gdpr.urls")),
    re_path(r"^invoice/", view=include("invoice.urls")),
    re_path(r"^mail/", view=include("mail.urls")),
    re_path(r"^search/", view=include("search.urls")),
    re_path(r"^sitemap\.xml$", view=sitemap, kwargs={"sitemaps": sitemaps}),
    re_path(r"^token/$", view=views.obtain_auth_token, name="api.token.auth"),
    re_path(r"^wizard/", view=include("block.urls.wizard")),
    re_path(r"^", view=include("web.urls")),
    # this url include should come last
    re_path(r"^", view=include("block.urls.cms")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#   ^ helper function to return a URL pattern for serving files in debug mode.
# https://docs.djangoproject.com/en/1.5/howto/static-files/#serving-files-uploaded-by-a-user

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        re_path(r"^__debug__/", include(debug_toolbar.urls))
    ] + urlpatterns
