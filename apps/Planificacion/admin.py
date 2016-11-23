from django.contrib import admin
from .models import Etapas, Proyectos, Inspeccion

# Register your models here.
admin.site.register(Etapas)
admin.site.register(Proyectos)
admin.site.register(Inspeccion)
