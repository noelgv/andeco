from django.conf.urls import patterns, url
from .views import Finanzas

urlpatterns = patterns('',
	url(r'^finansas/$', Finanzas.as_view(), name='finansas'),
	url(r'^proyectoFinanzas/$', 'apps.finanzas.views.createProyecto', name='proyectoFinanzas'),

)
