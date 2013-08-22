from django.views.generic import TemplateView


class ProjectMixin(object):

    def get_context_data(self, **kwargs):
        context = super(ProjectMixin, self).get_context_data(**kwargs)
        context.update(dict(
            path=self.request.path,
        ))
        return context


class ContactView(ProjectMixin, TemplateView):
    template_name = 'project/contact.html'


class HomeView(ProjectMixin, TemplateView):
    template_name = 'project/home.html'


class PortfolioView(ProjectMixin, TemplateView):
    template_name = 'project/portfolio.html'


class SecureView(ProjectMixin, TemplateView):
    template_name = 'project/secure.html'


class TechnologyView(ProjectMixin, TemplateView):
    template_name = 'project/technology.html'
