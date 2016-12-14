from django.conf.urls import patterns, url
from .views import Finanzas, EditTrabajo, EditAsistencia, EditCurso

urlpatterns = patterns('',
	url(r'^finansas/$', Finanzas.as_view(), name='finansas'),
	url(r'^proyectoFinanzas/$', 'apps.finanzas.views.createProyecto', name='proyectoFinanzas'),
    url(r'^lista_finanzas/$', 'apps.finanzas.views.listadoFinanzas', name='lista_finanzas'),
    url(r'^delete_trabajo/(?P<id>\d+)$', 'apps.finanzas.views.eliminarTrabajo', name='delete_trabajo'),
    url(r'^editar_trabajo/(?P<pk>\d+)$', EditTrabajo.as_view(), name='editar_trabajo'),
    url(r'^lista_asistencia/$', 'apps.finanzas.views.listadoAsistencia', name='lista_asistencia'),
	url(r'^crear_asistencia/$', 'apps.finanzas.views.createAsistencia', name='crear_asistencia'),
    url(r'^delete_asistencia/(?P<id>\d+)$', 'apps.finanzas.views.eliminarAsistencia', name='delete_asistencia'),
    url(r'^editar_asistencia/(?P<pk>\d+)$', EditAsistencia.as_view(), name='editar_asistencia'),
    url(r'^lista_cursos/$', 'apps.finanzas.views.listadoCursos', name='lista_cursos'),
	url(r'^crear_curso/$', 'apps.finanzas.views.createCurso', name='crear_curso'),
    url(r'^delete_curso/(?P<id>\d+)$', 'apps.finanzas.views.eliminarCurso', name='delete_curso'),
    url(r'^editar_curso/(?P<pk>\d+)$', EditCurso.as_view(), name='editar_curso'),

)
