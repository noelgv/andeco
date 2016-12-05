from django.conf.urls import patterns, url
#from .views import CrearResponsables
from .views import ListadoResponsables, EditProyecto, EditInspecion

urlpatterns = patterns('',
    # url(r'^responsables/$', Juridica.as_view(), name='responsables'),
    url(r'^crear_responsables/$', 'apps.Planificacion.views.CrearResponsables', name='crear_responsables'),
    url(r'^listado_responsables/$', ListadoResponsables.as_view(), name='listado_responsables'),

    url(r'^crear_planificacion/$', 'apps.Planificacion.views.CrearPlanificacion', name='crear_planificacion'),
    url(r'^crear_etapa/(?P<pk>\d+)$', 'apps.Planificacion.views.CrearEtapa', name='crear_etapa'),
    url(r'^lista_etapas/(?P<pk>\d+)$', 'apps.Planificacion.views.listaEtapas', name='lista_etapas'),
    url(r'^lista_proyectos/$', 'apps.Planificacion.views.listadoProyectos', name='lista_proyectos'),
    url(r'^reporte_gantt/(?P<pk>\d+)$', 'apps.Planificacion.views.ReporteGantt', name='reporte_gantt'),
    url(r'^gantt_ajax/(?P<pk>\d+)$', 'apps.Planificacion.views.GanttAjax', name='gantt_ajax'),
    url(r'^delete_proyect/(?P<id>\d+)$', 'apps.Planificacion.views.eliminarProyecto', name='delete_proyect'),
    url(r'^editar_proyecto/(?P<pk>\d+)$', EditProyecto.as_view(), name='editar_proyecto'),
    url(r'^lista_inspeccion/(?P<pk>\d+)$', 'apps.Planificacion.views.listaInspeccion', name='lista_inspeccion'),
    url(r'^ajax_inspeccion/(?P<pk>\d+)$', 'apps.Planificacion.views.listaInspeccionAjax', name='ajax_inspeccion'),
    url(r'^crear_inspeccion/(?P<pk>\d+)$', 'apps.Planificacion.views.CrearInspeccion', name='crear_inspeccion'),
    url(r'^delete_inspeccion/(?P<id>\d+)$', 'apps.Planificacion.views.eliminarInspeccion', name='delete_inspeccion'),
    url(r'^editar_inspeccion/(?P<pk>\d+)$', EditInspecion.as_view(), name='editar_inspeccion'),



    )
