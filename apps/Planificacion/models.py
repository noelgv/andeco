from django.db import models


class Proyectos(models.Model):
	region = models.CharField(max_length=200)
	municipio = models.CharField(max_length=200)
	nombre_proyecto = models.CharField(max_length=200)
	responsable_proyecto = models.CharField(max_length=200)
	responsable_seguimiento = models.CharField(max_length=200)
	porcentage_global = models.CharField(max_length=200, null=True, blank=True)

	def __unicode__(self):
		return self.nombre_proyecto


class Etapas(models.Model):
	fecha_inicio = models.DateField()
	fecha_conclucion = models.DateField(max_length=200)
	nombre_etapa = models.CharField(max_length=200)
	avance = models.CharField(max_length=200)
	dias = models.IntegerField()
	observaciones = models.CharField(max_length=200)
	informe = models.CharField(max_length=200)
	proyecto = models.ForeignKey(Proyectos, null=True, blank=True)
	
	def __unicode__(self):
		return self.nombre_etapa


class Responsables(models.Model):
	nombre = models.CharField(max_length=200)
	codigo = models.CharField(max_length=200)
	ci = models.CharField(max_length=200)
	telefono = models.CharField(max_length=200)
	direccion = models.CharField(max_length=200)
	proyecto = models.ForeignKey(Proyectos, null=True, blank=True)

	def __unicode__(self):
		return self.nombre
