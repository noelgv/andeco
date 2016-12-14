# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finanzas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asistencia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.CharField(max_length=200)),
                ('nombre', models.CharField(max_length=200)),
                ('region', models.CharField(max_length=200)),
                ('municipio', models.CharField(max_length=200)),
                ('responsable', models.CharField(max_length=200)),
                ('fecha_inicio', models.DateField(null=True, blank=True)),
                ('fecha_conclucion', models.DateField(null=True, blank=True)),
                ('objetivo', models.CharField(max_length=200)),
                ('estado', models.CharField(max_length=200, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cursos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField(null=True, blank=True)),
                ('titulo', models.CharField(max_length=200)),
                ('area', models.CharField(max_length=200)),
                ('costo', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
                ('duracion', models.CharField(max_length=200)),
                ('material', models.CharField(max_length=200)),
            ],
        ),
    ]
