# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Planificacion', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='etapas',
            old_name='cod',
            new_name='avance',
        ),
        migrations.RenameField(
            model_name='etapas',
            old_name='pocentaje',
            new_name='informe',
        ),
        migrations.RemoveField(
            model_name='proyectos',
            name='cod',
        ),
        migrations.AddField(
            model_name='etapas',
            name='dias',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='etapas',
            name='observaciones',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='etapas',
            name='proyecto',
            field=models.ForeignKey(blank=True, to='Planificacion.Proyectos', null=True),
        ),
        migrations.AddField(
            model_name='proyectos',
            name='municipio',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='proyectos',
            name='region',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='proyectos',
            name='responsable_proyecto',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='proyectos',
            name='responsable_seguimiento',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='responsables',
            name='proyecto',
            field=models.ForeignKey(blank=True, to='Planificacion.Proyectos', null=True),
        ),
        migrations.AlterField(
            model_name='proyectos',
            name='porcentage_global',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
    ]
