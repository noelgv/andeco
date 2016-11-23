# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Planificacion', '0007_auto_20161123_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyectos',
            name='porcentage_global',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
