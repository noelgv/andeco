# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Etapas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_inicio', models.DateField()),
                ('fecha_conclucion', models.DateField(max_length=200)),
                ('nombre_etapa', models.CharField(max_length=200)),
                ('cod', models.CharField(max_length=200)),
                ('pocentaje', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Proyectos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cod', models.DateField()),
                ('nombre_proyecto', models.CharField(max_length=200)),
                ('porcentage_global', models.CharField(max_length=200)),
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
            ],
        ),
    ]
