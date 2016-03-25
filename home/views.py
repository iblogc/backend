from django.shortcuts import render
from braces.views import LoginRequiredMixin
from django.views.generic import TemplateView


# Create your views here.
class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'home/index.html'

    def get(self, request, *args, **kwargs):
        return super(IndexView, self).get(request, *args, **kwargs)