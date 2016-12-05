from django.conf.urls import patterns, url
from.views import Index, loginview, Inicio, UserCreate

urlpatterns = patterns('',
	url(r'^$', Index.as_view(), name='index'),
    url(r'^inicio/$', Inicio.as_view(), name='inicio'),
	url(r'^salir/$', 'apps.inicio.views.logOut'),
	url(r'^login/$', loginview.as_view(), name='login'),
	url(r'^user_create/$', 'apps.inicio.views.UserCreate', name='user_create'),
	url(r'^lista_usuarios/$', 'apps.inicio.views.ListaUsuarios', name='lista_usuarios'),
	url(r'^delete_usuario/(?P<id>\d+)$', 'apps.inicio.views.eliminarUsuario', name='delete_usuario'),
	)
