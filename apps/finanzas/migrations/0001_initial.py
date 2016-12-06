# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='proyectoFinanzas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.CharField(max_length=200)),
                ('nombre_proyecto', models.CharField(max_length=200)),
                ('region', models.CharField(max_length=200)),
                ('municipio', models.CharField(max_length=200)),
                ('responsable_proyecto', models.CharField(max_length=200)),
                ('fecha_inicio', models.DateField(null=True, blank=True)),
                ('fecha_conclucion', models.DateField(null=True, blank=True)),
                ('objetivo', models.CharField(max_length=200)),
                ('avance', models.IntegerField(null=True, blank=True)),
            ],
        ),
    ]
