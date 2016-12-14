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


class Asistencia(models.Model):
	codigo = models.CharField(max_length=200)
	nombre = models.CharField(max_length=200)
	region = models.CharField(max_length=200)
	municipio = models.CharField(max_length=200)
	responsable = models.CharField(max_length=200)
	fecha_inicio = models.DateField(null=True, blank=True)
	fecha_conclucion = models.DateField(null=True, blank=True)
	objetivo = models.CharField(max_length=200)
	estado = models.CharField(max_length=200, null=True, blank=True)

	def __unicode__(self):
		return self.nombre


class Cursos(models.Model):
	fecha = models.DateField(null=True, blank=True)
	titulo = models.CharField(max_length=200)
	area = models.CharField(max_length=200)
	costo = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
	duracion = models.CharField(max_length=200)
	material = models.CharField(max_length=200)

	def __unicode__(self):
		return self.titulo
