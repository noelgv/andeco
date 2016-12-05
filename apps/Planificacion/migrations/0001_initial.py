# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Etapas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_inicio', models.DateField()),
                ('fecha_conclucion', models.DateField()),
                ('nombre_etapa', models.CharField(max_length=200)),
                ('avance', models.CharField(max_length=200)),
                ('dias', models.IntegerField()),
                ('observaciones', models.CharField(max_length=200)),
                ('informe', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Inspeccion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
                ('objectivo', models.CharField(max_length=200)),
                ('avance', models.CharField(max_length=200)),
                ('etapa', models.ForeignKey(blank=True, to='Planificacion.Etapas', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Proyectos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('region', models.CharField(max_length=200)),
                ('municipio', models.CharField(max_length=200)),
                ('nombre_proyecto', models.CharField(max_length=200)),
                ('responsable_seguimiento', models.CharField(max_length=200)),
                ('porcentage_global', models.IntegerField(null=True, blank=True)),
                ('fecha_inicio', models.DateField(null=True, blank=True)),
                ('fecha_conclucion', models.DateField(null=True, blank=True)),
                ('responsable_proyecto', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Responsables',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=200)),
                ('codigo', models.CharField(max_length=200)),
                ('ci', models.CharField(max_length=200)),
                ('telefono', models.CharField(max_length=200)),
                ('direccion', models.CharField(max_length=200)),
                ('proyecto', models.ForeignKey(blank=True, to='Planificacion.Proyectos', null=True)),
            ],
        ),
        migrations.AddField(
            model_name='etapas',
            name='proyecto',
            field=models.ForeignKey(blank=True, to='Planificacion.Proyectos', null=True),
        ),
    ]
