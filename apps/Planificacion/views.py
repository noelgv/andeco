from django.shortcuts import render_to_response, render
from django.views.generic import TemplateView, FormView, ListView, UpdateView
from .forms import responsablesForm, proyectosForm, inspeccionForm
from django.core.urlresolvers import reverse_lazy
from .models import Responsables, Proyectos, Etapas, Inspeccion

from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
import json
from decimal import Decimal, ROUND_HALF_UP
from django.core.serializers.json import DjangoJSONEncoder
import datetime, time
from django import forms 


# Create your views here.
def CrearResponsables(request):
    if request.method == 'POST':
        form = responsablesForm(request.POST)
        if form.is_valid():
            responsables = Responsables(
                nombre = form.cleaned_data['nombre'],
                codigo = form.cleaned_data['codigo'],
                ci = form.cleaned_data['ci'],
                telefono = form.cleaned_data['telefono'],
                direccion = form.cleaned_data['direccion'])
            responsables.save()
            return HttpResponseRedirect(reverse_lazy('listado_responsables'))
    else:
        form = responsablesForm()
    variables = RequestContext(request, {'form': form})
    return render_to_response('planificacion/registro_responsable.html', variables)


class ListadoResponsables(ListView):
    model = Responsables
    template_name = 'planificacion/listado_responsables.html'


# class listadoProyectos(ListView):
#     model = Proyectos
#     template_name = 'planificacion/listado_Proyectos.html'


def listadoProyectos(request):
    proyectos = Proyectos.objects.all()
    porcentage = 0
    data = []
    for p in proyectos:
        etapas = Etapas.objects.filter(proyecto=p.pk)
        avance = 0
        cant_etapa = 0
        for e in etapas:
            cant_etapa = cant_etapa + 1
            avance = avance + Decimal(e.avance)
        print '------------'
        print avance
        print cant_etapa
        if avance != 0 and cant_etapa != 0:
            porcentage = avance / cant_etapa
            proyecto = Proyectos.objects.filter(pk=p.pk)
            proyecto.update(porcentage_global=porcentage)
        redondeado = Decimal(porcentage.quantize(Decimal('.01'), rounding=ROUND_HALF_UP))
        data.append({'pk': p.pk, 'region': p.region, 'municipio': p.municipio, 'nombre_proyecto': p.nombre_proyecto, 'responsable_proyecto': p.responsable_proyecto, 'responsable_seguimiento': p.responsable_seguimiento, 'porcentage_global': redondeado })

    variables = RequestContext(request, {'object_list': data})

    return render_to_response('planificacion/listado_Proyectos.html', variables)



def Crearproyecto(request):
    if request.method == 'POST':
        form = proyectosForm(request.POST)
        if form.is_valid():
            proyectos = Proyectos(
                nombre = form.cleaned_data['nombre'],
                codigo = form.cleaned_data['codigo'],
                porcentaje_global = form.cleaned_data['porcentaje_global'])
            proyectos.save()
            return HttpResponseRedirect(reverse_lazy('listado_responsables'))
    else:
        form = proyectosForm()
    variables = RequestContext(request, {'form': form})
    return render_to_response('proyectos/proyectos.html', variables)


def CrearPlanificacion(request):
    if request.method == 'POST':
        form = proyectosForm(request.POST)
        if form.is_valid():
            proyectos = Proyectos(
                region=form.cleaned_data['regiones'],
                municipio=form.cleaned_data['municipios'],
                nombre_proyecto=form.cleaned_data['nombre_proyecto'],
                responsable_proyecto=form.cleaned_data['responsable_proyecto'],
                responsable_seguimiento=form.cleaned_data['responsable_seguimiento'],
                porcentage_global=0,
                fecha_inicio=form.cleaned_data['fecha_inicio'],
                fecha_conclucion=form.cleaned_data['fecha_conclucion'])
               
            proyectos.save()
            return HttpResponseRedirect(reverse_lazy('crear_etapa', kwargs={'pk':proyectos.pk}))
    else:
        form = proyectosForm()
    variables = RequestContext(request, {'form': form})

    return render_to_response('planificacion/crear_planificacion.html', variables)


def CrearEtapa(request, pk):
    if request.method == 'POST':
        etapa = Etapas(
          fecha_inicio=request.POST['fecha_inicio'],
          fecha_conclucion=request.POST['fecha_conclucion'],
          nombre_etapa=request.POST['nombre_etapa'],
          avance=request.POST['avance'],
          dias=request.POST['dias'],
          observaciones=request.POST['observaciones'],
          informe=request.POST['informe'],
          proyecto=Proyectos.objects.get(id=pk))

        etapa.save()
        print 'llegoooo aaaaquiiii'
        data = {'pk': etapa.pk, 'fecha_inicio': etapa.fecha_inicio, 'fecha_conclucion': etapa.fecha_conclucion, 'nombre_etapa': etapa.nombre_etapa, 'avance': etapa.avance, 'dias': etapa.dias, 'observaciones': etapa.observaciones, 'informe': etapa.informe}
        print 'guardoooooooo'
        return HttpResponse(json.dumps(data), content_type='application/json')
    else:
        variables = RequestContext(request, {'pk': pk, 'proyecto': Proyectos.objects.get(id=pk)})
        return render_to_response('planificacion/crear_etapa.html', variables)


def listaEtapas(request, pk):
    etapas = Etapas.objects.filter(proyecto=pk)
    data = []
    for etapa in etapas:
        data.append({'pk': etapa.pk, 'fecha_inicio': etapa.fecha_inicio, 'fecha_conclucion': etapa.fecha_conclucion, 'nombre_etapa': etapa.nombre_etapa, 'avance': etapa.avance, 'dias': etapa.dias, 'observaciones': etapa.observaciones, 'informe': etapa.informe, 'responsable': etapa.proyecto.responsable_proyecto, 'seguimiento': etapa.proyecto.responsable_seguimiento, 'proyecto': etapa.proyecto.nombre_proyecto})

    json_data = json.dumps(data, cls=DjangoJSONEncoder)
    return HttpResponse(json_data, content_type="application/json")


# Create your views here.
def ReporteGantt(request, pk):
    proyecto = Proyectos.objects.get(pk=pk)
    variables = RequestContext(request, {'pk': pk, 'nombre_proyecto': proyecto.nombre_proyecto})
    return render_to_response('planificacion/reporte_gantt.html', variables)


def GanttAjax(request, pk):
    etapas = Etapas.objects.filter(proyecto=pk)
    data = []
    id_count = 0
    for etapa in etapas:
        id_count = id_count + 1
        print id_count
        p = 20 / 3
        progreso = float(etapa.avance) / float(100)
        fecha = datetime.datetime.strptime(str(etapa.fecha_inicio), '%Y-%m-%d').strftime("%d-%m-%Y")
        print progreso
        data.append({'id': id_count, 'text': etapa.nombre_etapa, 'start_date': fecha, 'duration': etapa.dias, 'order': 20, 'progress': progreso, 'parent': 0})

    json_data = json.dumps(data, cls=DjangoJSONEncoder)
    return HttpResponse(json_data, content_type="application/json")


def eliminarProyecto(request, id):
    p = Proyectos.objects.get(id=id)
    p.delete()
    return HttpResponseRedirect(reverse_lazy('lista_proyectos'))


class EditProyecto(UpdateView):
    template_name = "planificacion/edit_proyecto.html"
    model = Proyectos
    fields = ['region', 'municipio', 'nombre_proyecto', 'responsable_proyecto', 'responsable_seguimiento', 'fecha_inicio', 'fecha_conclucion']
    success_url = reverse_lazy('lista_proyectos')

    def get_form(self, form_class):
        form = super(EditProyecto, self).get_form(form_class)
        form.fields['fecha_inicio'].widget = forms.DateInput(format='%Y-%m-%d')
        form.fields['fecha_conclucion'].widget = forms.DateInput(format='%Y-%m-%d')
        return form
        

# Create your views here.
def listaInspeccion(request, pk):
    etapa = Etapas.objects.get(pk=pk)
    inspecciones = Inspeccion.objects.filter(etapa=pk)
    print time.strftime("%X")

    variables = RequestContext(request, {'pk': pk, 'etapa': etapa.nombre_etapa, 'proyecto': etapa.proyecto.nombre_proyecto,  'inspecciones': inspecciones})

    return render_to_response('planificacion/lista_inspeccion.html', variables)


def listaInspeccionAjax(request, pk):
    inspecciones = Inspeccion.objects.filter(etapa=pk)
    data = []
    for ins in inspecciones:
        data.append({'pk': ins.pk, 'fecha': ins.fecha, 'hora': ins.hora, 'objetivo': ins.objectivo, 'avance': ins.avance})

    json_data = json.dumps(data, cls=DjangoJSONEncoder)
    return HttpResponse(json_data, content_type="application/json")


def CrearInspeccion(request, pk):
    if request.method == 'POST':
        form = inspeccionForm(request.POST)
        if form.is_valid():
            inspeccion = Inspeccion(
                fecha=datetime.date.today(),
                hora=datetime.datetime.today().time(),
                objectivo=form.cleaned_data['objetivo'],
                avance=form.cleaned_data['avance'],
                etapa=Etapas.objects.get(pk=pk))
               
            inspeccion.save()
            etapa = Etapas.objects.filter(pk=pk)
            etapa.update(avance=inspeccion.avance)
            return HttpResponseRedirect(reverse_lazy('lista_inspeccion', kwargs={'pk':pk}))
    else:
        form = inspeccionForm()
    variables = RequestContext(request, {'form': form})

    return render_to_response('planificacion/crear_inspeccion.html', variables)


def eliminarInspeccion(request, id):
    p = Inspeccion.objects.get(id=id)
    pk = p.etapa.pk
    p.delete()
    return HttpResponseRedirect(reverse_lazy('lista_inspeccion', kwargs={'pk':pk}))

