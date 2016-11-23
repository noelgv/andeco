from django.conf.urls import patterns, url
from .views import municipios, Crearmunicipios, Crearprovincias, provincias

urlpatterns = patterns('',
    url(r'^municipios/$', municipios.as_view(), name='municipios'),
    url(r'^crear_municipio/$', Crearmunicipios.as_view(), name='crear_municipio'),
    url(r'^provincia/$', provincias.as_view(), name='provincia'),
    url(r'^crear_provincia/$', Crearprovincias.as_view(), name='crear_provincia'),

    )
