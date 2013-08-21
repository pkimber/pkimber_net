from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'project/home.html'


class SecureView(TemplateView):
    template_name = 'project/secure.html'
