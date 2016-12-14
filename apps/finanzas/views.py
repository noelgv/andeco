from django.shortcuts import render_to_response, render
from django.views.generic import TemplateView, UpdateView
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse_lazy
from .models import proyectoFinanzas, Asistencia, Cursos
from .forms import createProyectForm, AsistenciaForm, CursoForm
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


def listadoAsistencia(request):
    print request.user.pk
    asistencia = Asistencia.objects.all()
    variables = RequestContext(request, {'asistencia': asistencia})

    return render_to_response('finanzas/listado_asistencia.html', variables)


def createAsistencia(request):
    if request.method == 'POST':
        form = AsistenciaForm(request.POST)
        if form.is_valid():
            print 'sdfdsfdsfdsfds'
            asistencia = Asistencia(
                codigo=form.cleaned_data['codigo'],
                nombre=form.cleaned_data['nombre'],
                region=form.cleaned_data['region'],
                municipio=form.cleaned_data['municipio'],
                responsable=form.cleaned_data['responsable'],
                fecha_inicio=form.cleaned_data['fecha_inicio'],
                fecha_conclucion=form.cleaned_data['fecha_conclucion'],
                objetivo=form.cleaned_data['objetivo'],
                estado=form.cleaned_data['estado'])
            asistencia.save()

            return HttpResponseRedirect(reverse_lazy('lista_asistencia'))
    else:
        form = AsistenciaForm()
    variables = RequestContext(request, {'form': form})
    return render_to_response('finanzas/crear_asistencia.html', variables)


def eliminarAsistencia(request, id):
    p = Asistencia.objects.get(id=id)
    p.delete()
    return HttpResponseRedirect(reverse_lazy('lista_asistencia'))


class EditAsistencia(UpdateView):
    template_name = "finanzas/edit_asistencia.html"
    model = Asistencia
    fields = ['codigo', 'nombre', 'region', 'municipio', 'responsable', 'fecha_inicio', 'fecha_conclucion', 'objetivo', 'estado']
    success_url = reverse_lazy('lista_asistencia')

    def get_form(self, form_class):
        form = super(EditAsistencia, self).get_form(form_class)
        form.fields['fecha_inicio'].widget = forms.DateInput(format='%Y-%m-%d')
        form.fields['fecha_conclucion'].widget = forms.DateInput(format='%Y-%m-%d')
        return form

def listadoCursos(request):
    print request.user.pk
    cursos = Cursos.objects.all()
    variables = RequestContext(request, {'cursos': cursos})

    return render_to_response('finanzas/listado_cursos.html', variables)


def createCurso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            print 'sdfdsfdsfdsfds'
            curso = Cursos(
                fecha=form.cleaned_data['fecha'],
                titulo=form.cleaned_data['titulo'],
                area=form.cleaned_data['area'],
                costo=form.cleaned_data['costo'],
                duracion=form.cleaned_data['duracion'],
                material=form.cleaned_data['material'])
            curso.save()

            return HttpResponseRedirect(reverse_lazy('lista_cursos'))
    else:
        form = CursoForm()
    variables = RequestContext(request, {'form': form})
    return render_to_response('finanzas/crear_curso.html', variables)


def eliminarCurso(request, id):
    p = Cursos.objects.get(id=id)
    p.delete()
    return HttpResponseRedirect(reverse_lazy('lista_cursos'))


class EditCurso(UpdateView):
    template_name = "finanzas/edit_curso.html"
    model = Cursos
    fields = ['fecha', 'titulo', 'area', 'costo', 'duracion', 'material']
    success_url = reverse_lazy('lista_cursos')

    def get_form(self, form_class):
        form = super(EditCurso, self).get_form(form_class)
        form.fields['fecha'].widget = forms.DateInput(format='%Y-%m-%d')
        return form
