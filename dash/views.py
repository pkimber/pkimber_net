# -*- encoding: utf-8 -*-
from django.views.generic import DetailView, TemplateView

from braces.views import LoginRequiredMixin, StaffuserRequiredMixin

from base.view_utils import BaseMixin
from crm.views import CrmContactDetailMixin


class ContactDetailView(
        LoginRequiredMixin, CrmContactDetailMixin, BaseMixin, DetailView):
    pass


class HomeView(
        LoginRequiredMixin, StaffuserRequiredMixin, BaseMixin, TemplateView):

    template_name = 'dash/home.html'


class SettingsView(
        LoginRequiredMixin, StaffuserRequiredMixin, BaseMixin, TemplateView):

    template_name = 'dash/settings.html'
