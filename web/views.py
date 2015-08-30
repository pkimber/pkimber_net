# -*- encoding: utf-8 -*-
from django.views.generic import CreateView

from block.views import (
    CmsMixin,
    PageFormMixin,
)
from enquiry.forms import EnquiryForm
from enquiry.views import Enquiry


class EnquiryCreateView(CmsMixin, PageFormMixin, CreateView):

    form_class = EnquiryForm
    model = Enquiry

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update(dict(
            request=self.request,
            user=self.request.user,
        ))
        return kwargs

    def get_success_url(self):
        page = Page.objects.get(slug='contact', slug_menu='thankyou')
        return page.get_absolute_url()
