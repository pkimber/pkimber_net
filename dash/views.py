from __future__ import unicode_literals

from django.views.generic import TemplateView

from braces.views import (
    LoginRequiredMixin,
    StaffuserRequiredMixin,
)


class HomeView(
        LoginRequiredMixin, StaffuserRequiredMixin, TemplateView):

    template_name = 'dash/home.html'
