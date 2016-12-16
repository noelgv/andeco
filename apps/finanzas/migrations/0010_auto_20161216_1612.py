# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finanzas', '0009_cursos_region'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cursos',
            old_name='fecha',
            new_name='fecha_conclucion',
        ),
        migrations.RenameField(
            model_name='cursos',
            old_name='duracion',
            new_name='objetivo',
        ),
        migrations.AddField(
            model_name='cursos',
            name='fecha_inicio',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='cursos',
            name='responsable',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
