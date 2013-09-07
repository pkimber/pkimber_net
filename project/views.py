from django.views.generic import ListView, TemplateView

from cms.models import Simple
from base.view_utils import BaseMixin


class ContactView(BaseMixin, TemplateView):
    template_name = 'project/contact.html'


class HomeView(BaseMixin, ListView):
    queryset = Simple.objects.filter(
        moderated=True,
        section__name='home',
    ).order_by(
        'order',
        'modified',
    )
    template_name = 'project/home_list.html'


class PortfolioView(BaseMixin, ListView):
    queryset = Simple.objects.filter(
        moderated=True,
        section__name='portfolio',
    ).order_by(
        'order',
        'modified',
    )
    template_name = 'project/portfolio_list.html'


class TechnologyView(BaseMixin, ListView):
    queryset = Simple.objects.filter(
        moderated=True,
        section__name='tech',
    ).order_by(
        'order',
        'modified',
    )
    template_name = 'project/technology_list.html'
