import os

from django.db.models import Sum, Value, F
from django.db.models.functions import Coalesce
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.views import generic

from consumptions.form import ConsumptionForm
from consumptions.models import Consumption


class ConsumptionListView(generic.ListView):
    model = Consumption
    template_name = "consumptions/consumption_list.html"
    context_object_name = 'consumo_list'

    def get_context_data(self, **kwargs):
        query = Consumption.objects.filter(id__isnull=True)
        # query = Consumption.objects.none().values_list('id').order_by('id')
        context = super().get_context_data(**kwargs)
        if query:
            context['sumaMonto'] = Consumption.objects.all().aggregate(Sum('monto'))['monto__sum' or 00.0]
            odo_ini = Consumption.objects.values('odometro').first()['odometro']
            odo_fin = Consumption.objects.values('odometro').last()['odometro']
            context['odo'] = odo_fin - odo_ini
        return context


class ConsumptionCreateView(CreateView):
    model = Consumption
    form_class = ConsumptionForm
    success_url = reverse_lazy('consumptions:consumptions')


class ConsumptionsDetailView(generic.DetailView):
    model = Consumption
    template_name = 'consumptions/consumption_detail.html'

    # def get_context_data(self, **kwargs):
    #     # xxx will be available in the template as the related objects
    #     context = super(ConsumptionsDetailView, self).get_context_data(**kwargs)
    #     context['prueba'] = Consumption.objects.values('monto')
    #     return context

    # def get_object(self):
    #     """Returns the BlogPost instance that the view displays"""
    #     return get_object_or_404(Consumption, pk=self.kwargs.get("pk"))

    #
    # def get_queryset(self):
    #     if self.request.GET.get("prueba"):
    #         return Consumption.objects.all()
    #     else:
    #         return Consumption.objects.values('odometro')

    # def get_context_data(self, **kwargs):
    #     context = super(ConsumptionsDetailView, self).get_context_data(**kwargs)
    #     context['prueba'] = Consumption.objects.values('odometro')[0]
    #     return context
    def get_context_data(self, **kwargs):
        """Insert the single object into the context dict."""
        context = {}
        if self.object:
            precio_x_litro = self.get_object(Consumption.objects.values('precio_litro'))['precio_litro' or 0]
            monto_total = self.get_object(Consumption.objects.values('monto'))['monto' or 0]
            context['litros'] = monto_total / precio_x_litro
            context_object_name = self.get_context_object_name(self.object)
            if context_object_name:
                context[context_object_name] = self.object
        context.update(kwargs)
        return super(ConsumptionsDetailView, self).get_context_data(**context)


class ConsumptionUpdateView(UpdateView):
    model = Consumption
    form_class = ConsumptionForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('consumptions:update', args=[self.object.id]) + '?ok'


class ConsumptionDeleteView(DeleteView):
    model = Consumption
    success_url = reverse_lazy('consumptions:consumptions')
