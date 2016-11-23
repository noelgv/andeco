from django.db import models


class Municipios(models.Model):
	cod_municipio = models.CharField(max_length=20)
	nombre = models.CharField(max_length=200)

	def __unicode__(self):
		return self.nombre


class Provincia(models.Model):
	cod_provincia = models.CharField(max_length=20)
	nombre = models.CharField(max_length=200)
	municipio = models.ForeignKey(Municipios, null=True, blank=True)

	def __unicode__(self):
		return self.nombre
