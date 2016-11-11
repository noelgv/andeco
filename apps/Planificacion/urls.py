from django.conf.urls import patterns, url
#from .views import CrearResponsables
from .views import ListadoResponsables, listadoProyectos

urlpatterns = patterns('',
    # url(r'^responsables/$', Juridica.as_view(), name='responsables'),
    url(r'^crear_responsables/$', 'apps.Planificacion.views.CrearResponsables', name='crear_responsables'),
    url(r'^listado_responsables/$', ListadoResponsables.as_view(), name='listado_responsables'),

    url(r'^crear_planificacion/$', 'apps.Planificacion.views.CrearPlanificacion', name='crear_planificacion'),
    url(r'^crear_etapa/(?P<pk>\d+)$', 'apps.Planificacion.views.CrearEtapa', name='crear_etapa'),
    url(r'^lista_etapas/(?P<pk>\d+)$', 'apps.Planificacion.views.listaEtapas', name='lista_etapas'),
    url(r'^lista_proyectos/$', listadoProyectos.as_view(), name='lista_proyectos'),
    url(r'^reporte_gantt/(?P<pk>\d+)$', 'apps.Planificacion.views.ReporteGantt', name='reporte_gantt'),
    url(r'^gantt_ajax/(?P<pk>\d+)$', 'apps.Planificacion.views.GanttAjax', name='gantt_ajax'),


    )
