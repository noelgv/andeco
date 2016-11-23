# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('juridica', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='convenios',
            name='contra_financiera',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='convenios',
            name='entidad',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='convenios',
            name='fecha',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='convenios',
            name='objetivo',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='convenios',
            name='vig_avance',
            field=models.CharField(max_length=200),
        ),
    ]
