from django.views.generic import ListView, TemplateView

from base.view_utils import BaseMixin
from cms.models import Section
from .models import StripeContent


LAYOUT_SLUG = 'body'


class ContactView(BaseMixin, TemplateView):
    template_name = 'project/contact.html'


class HomeView(BaseMixin, ListView):

    template_name = 'project/home_list.html'

    def get_queryset(self):
        section = Section.objects.get(
            page__slug='home',
            layout__slug=LAYOUT_SLUG,
        )
        return StripeContent.objects.published(section)


class PortfolioView(BaseMixin, ListView):

    template_name = 'project/portfolio_list.html'

    def get_queryset(self):
        section = Section.objects.get(
            page__slug='portfolio',
            layout__slug=LAYOUT_SLUG,
        )
        return StripeContent.objects.published(section)


class TechnologyView(BaseMixin, ListView):

    template_name = 'project/technology_list.html'

    def get_queryset(self):
        section = Section.objects.get(
            page__slug='tech',
            layout__slug=LAYOUT_SLUG,
        )
        return StripeContent.objects.published(section)
