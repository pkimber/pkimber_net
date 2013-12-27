from django.views.generic import ListView, TemplateView

from cms.models import (
    ModerateState,
    Section,
)
from base.view_utils import BaseMixin


class ContactView(BaseMixin, TemplateView):
    template_name = 'project/contact.html'


class HomeView(BaseMixin, ListView):
    queryset = Section.objects.filter(
        moderate_state=ModerateState.published(),
        page__name='home',
    ).order_by(
        'order',
        'modified',
    )
    template_name = 'project/home_list.html'


class PortfolioView(BaseMixin, ListView):
    queryset = Section.objects.filter(
        moderate_state=ModerateState.published(),
        page__name='portfolio',
    ).order_by(
        'order',
        'modified',
    )
    template_name = 'project/portfolio_list.html'


class TechnologyView(BaseMixin, ListView):
    queryset = Section.objects.filter(
        moderate_state=ModerateState.published(),
        page__name='tech',
    ).order_by(
        'order',
        'modified',
    )
    template_name = 'project/technology_list.html'


class TempView(TemplateView):

    template_name = 'project/index.html'
