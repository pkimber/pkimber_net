from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'project/home.html'


class PortfolioView(TemplateView):
    template_name = 'project/portfolio.html'


class SecureView(TemplateView):
    template_name = 'project/secure.html'
