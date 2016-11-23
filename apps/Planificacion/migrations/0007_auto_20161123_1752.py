# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Planificacion', '0006_auto_20161123_1659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyectos',
            name='porcentage_global',
            field=models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True),
        ),
    ]
