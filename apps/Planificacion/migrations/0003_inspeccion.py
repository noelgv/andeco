# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Planificacion', '0002_auto_20161114_2019'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inspeccion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField()),
                ('hora', models.DateField()),
                ('objectivo', models.CharField(max_length=200)),
                ('avance', models.CharField(max_length=200)),
                ('etapa', models.ForeignKey(blank=True, to='Planificacion.Etapas', null=True)),
            ],
        ),
    ]
