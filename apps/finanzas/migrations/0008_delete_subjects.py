# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finanzas', '0007_subjects'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Subjects',
        ),
    ]
