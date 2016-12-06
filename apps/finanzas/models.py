from django.db import models


class proyectoFinanzas(models.Model):
	codigo = models.CharField(max_length=200)
	nombre_proyecto = models.CharField(max_length=200)
	region = models.CharField(max_length=200)
	municipio = models.CharField(max_length=200)
	responsable_proyecto = models.CharField(max_length=200)
	fecha_inicio = models.DateField(null=True, blank=True)
	fecha_conclucion = models.DateField(null=True, blank=True)
	objetivo = models.CharField(max_length=200)
	avance = models.IntegerField(null=True, blank=True)

	def __unicode__(self):
		return self.nombre_proyecto
