from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "core/index.html"

    # def get(self, request, *args, **kwargs):
    #     return render(request, self.template_name, {'name': "Calmao"})
    #
