from django.conf.urls import patterns, url
from .views import Finanzas, EditTrabajo

urlpatterns = patterns('',
	url(r'^finansas/$', Finanzas.as_view(), name='finansas'),
	url(r'^proyectoFinanzas/$', 'apps.finanzas.views.createProyecto', name='proyectoFinanzas'),
    url(r'^lista_finanzas/$', 'apps.finanzas.views.listadoFinanzas', name='lista_finanzas'),
    url(r'^delete_trabajo/(?P<id>\d+)$', 'apps.finanzas.views.eliminarTrabajo', name='delete_trabajo'),
    url(r'^editar_trabajo/(?P<pk>\d+)$', EditTrabajo.as_view(), name='editar_trabajo'),

)
