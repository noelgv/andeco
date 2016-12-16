# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finanzas', '0003_cursos_choice_field'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subjects',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('subject', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='cursos',
            name='choice_field',
        ),
        migrations.AddField(
            model_name='cursos',
            name='choice_field',
            field=models.ManyToManyField(to='finanzas.Subjects', blank=True),
        ),
    ]
