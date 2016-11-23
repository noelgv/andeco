from django.conf.urls import patterns, url
from.views import Index, loginview, Inicio

urlpatterns = patterns('',
	url(r'^$', Index.as_view(), name='index'),
    url(r'^inicio/$', Inicio.as_view(), name='inicio'),
	url(r'^salir/$', 'apps.inicio.views.logOut'),
	url(r'^login/$', loginview.as_view(), name='login'),
	
	)
