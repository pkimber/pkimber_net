# -*- encoding: utf-8 -*-
from django.views.generic import CreateView

from block.models import Page
from block.views import CmsMixin, PageFormMixin, PageTemplateView
from enquiry.views import EnquiryCreateMixin


class CmsHomePageView(CmsMixin, PageTemplateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(dict(twitter="pkimber"))
        return context


class EnquiryCreateView(
    EnquiryCreateMixin, CmsMixin, PageFormMixin, CreateView
):

    """Save an enquiry in the database."""

    def get_success_url(self):
        page = Page.objects.get(slug="contact", slug_menu="thankyou")
        return page.get_absolute_url()
