# -*- encoding: utf-8 -*-
from django.views.generic import CreateView

from braces.views import (
    LoginRequiredMixin,
    StaffuserRequiredMixin,
)

from block.forms import ContentEmptyForm
from block.models import Page
from block.views import (
    ContentCreateView,
    ContentPublishView,
    ContentRemoveView,
    ContentUpdateView,
    PageFormMixin,
)
from enquiry.forms import EnquiryForm
from enquiry.views import Enquiry

from .forms import MainForm
from .models import (
    Main,
    MainBlock,
)


class EnquiryCreateView(PageFormMixin, CreateView):

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


class MainCreateView(
        LoginRequiredMixin, StaffuserRequiredMixin, ContentCreateView):

    block_class = MainBlock
    form_class = MainForm
    model = Main
    template_name = 'web/main_create_update.html'


class MainPublishView(
        LoginRequiredMixin, StaffuserRequiredMixin, ContentPublishView):

    form_class = ContentEmptyForm
    model = Main
    template_name = 'web/main_publish.html'


class MainUpdateView(
        LoginRequiredMixin, StaffuserRequiredMixin, ContentUpdateView):

    form_class = MainForm
    model = Main
    template_name = 'web/main_create_update.html'


class MainRemoveView(
        LoginRequiredMixin, StaffuserRequiredMixin, ContentRemoveView):

    form_class = ContentEmptyForm
    model = Main
    template_name = 'web/main_remove.html'
