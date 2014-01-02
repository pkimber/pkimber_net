from django.views.generic import ListView, TemplateView

from base.view_utils import BaseMixin
from cms.models import (
    Content,
    Page,
)


class ContactView(BaseMixin, TemplateView):
    template_name = 'project/contact.html'


class HomeView(BaseMixin, ListView):

    template_name = 'project/home_list.html'

    def get_queryset(self):
        page = Page.objects.get(name='home')
        return Content.objects.published(page=page)


class PortfolioView(BaseMixin, ListView):

    template_name = 'project/portfolio_list.html'

    def get_queryset(self):
        page = Page.objects.get(name='portfolio')
        return Content.objects.published(page=page)


class TechnologyView(BaseMixin, ListView):

    template_name = 'project/technology_list.html'

    def get_queryset(self):
        page = Page.objects.get(name='tech')
        return Content.objects.published(page=page)
