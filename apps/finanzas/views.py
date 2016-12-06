from django.shortcuts import render_to_response, render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse_lazy
from .models import proyectoFinanzas
from .forms import createProyectForm
from django.template import RequestContext


# Create your views here.
class Finanzas(TemplateView):
    template_name = 'finanzas/lista.html'


def createProyecto(request):
    if request.method == 'POST':
        form = createProyectForm(request.POST)
        if form.is_valid():
            print 'sdfdsfdsfdsfds'
            proyectos = proyectoFinanzas(
                codigo=form.cleaned_data['codigo'],
                nombre_proyecto=form.cleaned_data['nombre_proyecto'],
                region=form.cleaned_data['region'],
                municipio=form.cleaned_data['municipio'],
                responsable_proyecto=form.cleaned_data['responsable_proyecto'],
                fecha_inicio=form.cleaned_data['fecha_inicio'],
                fecha_conclucion=form.cleaned_data['fecha_conclucion'],
                objetivo=form.cleaned_data['objetivo'],
                avance=form.cleaned_data['avance'])
            proyectos.save()



            return HttpResponseRedirect(reverse_lazy('listado_finanzas'))
    else:
        form = createProyectForm()
    variables = RequestContext(request, {'form': form})
    return render_to_response('finanzas/crear_proyectos.html', variables)
