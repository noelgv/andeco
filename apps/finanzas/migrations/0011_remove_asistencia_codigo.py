# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finanzas', '0010_auto_20161216_1612'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='asistencia',
            name='codigo',
        ),
    ]
