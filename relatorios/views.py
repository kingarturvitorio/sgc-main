from django.urls import reverse_lazy
from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from pacientes.models import Paciente
from calendario.models import Event
# Create your views here.

from django.views.generic.base import View
import xhtml2pdf.pisa as pisa
import io
from django.template.loader import get_template
from django.http import HttpResponse, HttpRequest

class RelatorioView(ListView):
    model = Paciente
    template_name = 'relatorio-list.html'
    context_object_name = 'pacientes'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        nome = self.request.GET.get('nome')

        if nome:
            queryset = queryset.filter(nome__icontains=nome)
        return queryset
    

def rel_aso(request, id):
    paciente = Paciente.objects.get(id=id)
    terapia = Event.objects.get(id=id)
    params = {
        'paciente': paciente,
        'terapia': terapia,
        'request': request,
    }
    return Render.render('rel_aso.html', params, 'rel-aso')

class Render:
    @staticmethod
    def render(path: str, params: dict, filename: str):
        template = get_template(path)
        html = template.render(params)
        response = io.BytesIO()
        pdf = pisa.pisaDocument(io.BytesIO(html.encode("UTF-8")), response)
        if not pdf.err:
            response = HttpResponse(response.getvalue(), content_type='application/pdf')
            response['Content-Disposition'] = 'attachment;filename=%s.pdf' % filename
            return response
        else:
            return HttpResponse("Error Rendering PDF", status=400)