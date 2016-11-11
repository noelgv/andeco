from django.shortcuts import render
from django.views.generic import TemplateView, FormView, ListView
from .forms import ConveniosForm
from django.core.urlresolvers import reverse_lazy
from .models import Convenios

# Create your views here.
class Juridica(ListView):
    model = Convenios
    template_name = 'juridica/lista.html'

class CrearConvenio(FormView):
    template_name = 'juridica/registro.html'
    form_class = ConveniosForm
    success_url = reverse_lazy('juridica')

    def form_valid(self, form):
        convenio = Convenios()
        convenio.fecha = form.cleaned_data['fecha']
        convenio.entidad = form.cleaned_data['entidad']
        convenio.objetivo = form.cleaned_data['objetivo']
        convenio.contra_financiera = form.cleaned_data['contra_financiera']
        convenio.vig_avance = form.cleaned_data['vig_avance']
        convenio.save()
        return super(CrearConvenio, self).form_valid(form)
