from django.shortcuts import render
from django.views.generic import TemplateView, FormView, ListView
from .forms import municipiosForm, provinciasForm
from django.core.urlresolvers import reverse_lazy
from .models import Municipios, Provincia

# Create your views here.
class municipios(ListView):
    model = Municipios
    template_name = 'municipios/lista.html'

class provincias(ListView):
    model = Provincia
    template_name = 'municipios/lista_provincias.html'

class Crearmunicipios(FormView):
    template_name = 'municipios/registro.html'
    form_class = municipiosForm
    success_url = reverse_lazy('municipios')

    def form_valid(self, form):
        municipio = Municipios()
        municipio.cod_municipio = form.cleaned_data['cod_municipio']
        municipio.nombre = form.cleaned_data['nombre']
        municipio.save()
        return super(Crearmunicipios, self).form_valid(form)

class Crearprovincias(FormView):
    template_name = 'municipios/registro_provincia.html'
    form_class = provinciasForm
    success_url = reverse_lazy('provincia')

    def form_valid(self, form):
        provincias = Provincia()
        provincias.cod_provincia = form.cleaned_data['cod_provincia']
        provincias.nombre = form.cleaned_data['nombre']
        provincias.save()
        return super(Crearprovincias, self).form_valid(form)
