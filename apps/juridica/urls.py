from django.conf.urls import patterns, url
from .views import Juridica, CrearConvenio

urlpatterns = patterns('',
    url(r'^juridica/$', Juridica.as_view(), name='juridica'),
    url(r'^crear_convenio/$', CrearConvenio.as_view(), name='crear_convenio'),

    )
