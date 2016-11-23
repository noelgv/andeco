from django.db import models


class contratos(models.Model):
    codigo = models.CharField(max_length=54)
    unidad = models.CharField(max_length=54)
    descripcion = models.CharField(max_length=64)

    def __unicode__(self):
        return self.codigo

