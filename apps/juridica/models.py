from django.db import models


class Convenios(models.Model):
    fecha = models.DateField()
    entidad = models.CharField(max_length=200)
    objetivo = models.CharField(max_length=200)
    contra_financiera = models.CharField(max_length=200)
    vig_avance = models.CharField(max_length=200)

    def __unicode__(self):
        return self.entidad

