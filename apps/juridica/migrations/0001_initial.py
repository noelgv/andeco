# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='convenios',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.CharField(max_length=84)),
                ('entidad', models.CharField(max_length=84)),
                ('objetivo', models.CharField(max_length=84)),
                ('contra_financiera', models.CharField(max_length=84)),
                ('vig_avance', models.CharField(max_length=87)),
            ],
        ),
    ]
