# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finanzas', '0008_delete_subjects'),
    ]

    operations = [
        migrations.AddField(
            model_name='cursos',
            name='region',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
