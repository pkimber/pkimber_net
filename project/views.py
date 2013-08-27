from django.views.generic import ListView, TemplateView

from cms.models import Simple


class ProjectMixin(object):

    def get_context_data(self, **kwargs):
        context = super(ProjectMixin, self).get_context_data(**kwargs)
        context.update(dict(
            path=self.request.path,
        ))
        return context


class ContactView(ProjectMixin, TemplateView):
    template_name = 'project/contact.html'


class HomeView(ProjectMixin, ListView):
    queryset = Simple.objects.filter(
        moderated=True,
        section__name='home',
    ).order_by(
        'order',
        'modified',
    )
    template_name = 'project/home_list.html'


class PortfolioView(ProjectMixin, ListView):
    queryset = Simple.objects.filter(
        moderated=True,
        section__name='portfolio',
    ).order_by(
        'order',
        'modified',
    )
    template_name = 'project/portfolio_list.html'


class SecureView(ProjectMixin, TemplateView):
    template_name = 'project/secure.html'


class TechnologyView(ProjectMixin, ListView):
    queryset = Simple.objects.filter(
        moderated=True,
        section__name='tech',
    ).order_by(
        'order',
        'modified',
    )
    template_name = 'project/technology_list.html'
