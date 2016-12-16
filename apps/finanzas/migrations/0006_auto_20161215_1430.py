# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finanzas', '0005_cursos_municipios'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cursos',
            name='choice_field',
        ),
        migrations.DeleteModel(
            name='Subjects',
        ),
    ]
