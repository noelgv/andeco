from django.shortcuts import render_to_response, render
from django.views.generic import TemplateView, UpdateView
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse_lazy
from .models import proyectoFinanzas
from .forms import createProyectForm
from django.template import RequestContext
from django import forms


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



            return HttpResponseRedirect(reverse_lazy('lista_finanzas'))
    else:
        form = createProyectForm()
    variables = RequestContext(request, {'form': form})
    return render_to_response('finanzas/crear_proyectos.html', variables)


def listadoFinanzas(request):
    print request.user.pk

    proyectos = proyectoFinanzas.objects.all()

    variables = RequestContext(request, {'proyectos': proyectos})

    return render_to_response('finanzas/listado_finanzas.html', variables)


def eliminarTrabajo(request, id):
    p = proyectoFinanzas.objects.get(id=id)
    p.delete()
    return HttpResponseRedirect(reverse_lazy('lista_finanzas'))



class EditTrabajo(UpdateView):
    template_name = "finanzas/edit_trabajo.html"
    model = proyectoFinanzas
    fields = ['codigo', 'nombre_proyecto', 'region', 'municipio', 'responsable_proyecto', 'fecha_inicio', 'fecha_conclucion', 'objetivo', 'avance']
    success_url = reverse_lazy('lista_finanzas')

    def get_form(self, form_class):
        form = super(EditTrabajo, self).get_form(form_class)
        form.fields['fecha_inicio'].widget = forms.DateInput(format='%Y-%m-%d')
        form.fields['fecha_conclucion'].widget = forms.DateInput(format='%Y-%m-%d')
        return form
