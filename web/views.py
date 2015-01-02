# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from braces.views import (
    LoginRequiredMixin,
    StaffuserRequiredMixin,
)

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
