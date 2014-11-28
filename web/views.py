# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import ListView, TemplateView

from braces.views import (
    LoginRequiredMixin,
    StaffuserRequiredMixin,
)

from base.view_utils import BaseMixin
from block.forms import ContentEmptyForm
from block.views import (
    ContentCreateView,
    ContentPublishView,
    ContentRemoveView,
    ContentUpdateView,
)

from .forms import MainForm
from .models import (
    Main,
    MainBlock,
)


#LAYOUT_SLUG = 'body'


#class ContactView(BaseMixin, TemplateView):
#    template_name = 'project/contact.html'
#
#
#class HomeView(BaseMixin, ListView):
#
#    template_name = 'project/home_list.html'
#
#    def get_queryset(self):
#        section = Section.objects.get(
#            page__slug='home',
#            layout__slug=LAYOUT_SLUG,
#        )
#        return StripeContent.objects.published(section)
#
#
#class PortfolioView(BaseMixin, ListView):
#
#    template_name = 'project/portfolio_list.html'
#
#    def get_queryset(self):
#        section = Section.objects.get(
#            page__slug='portfolio',
#            layout__slug=LAYOUT_SLUG,
#        )
#        return StripeContent.objects.published(section)
#
#
#class TechnologyView(BaseMixin, ListView):
#
#    template_name = 'project/technology_list.html'
#
#    def get_queryset(self):
#        section = Section.objects.get(
#            page__slug='tech',
#            layout__slug=LAYOUT_SLUG,
#        )
#        return StripeContent.objects.published(section)


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

    def post(self, request, *args, **kwargs):
        print('POST, POST')
        return super(MainUpdateView, self).post(request, *args, **kwargs)

    def form_invalid(self, form):
        print('form_invalid')
        return super(MainUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        print('form_valid')
        self.object = form.save(commit=False)
        return super(MainUpdateView, self).form_valid(form)


class MainRemoveView(
        LoginRequiredMixin, StaffuserRequiredMixin, ContentRemoveView):

    form_class = ContentEmptyForm
    model = Main
    template_name = 'web/main_remove.html'
