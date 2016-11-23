# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Planificacion', '0003_inspeccion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inspeccion',
            name='hora',
            field=models.TimeField(),
        ),
    ]
