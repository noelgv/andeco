# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Planificacion', '0004_auto_20161121_1539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyectos',
            name='porcentage_global',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
