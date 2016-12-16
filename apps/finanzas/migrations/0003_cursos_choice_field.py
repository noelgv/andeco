# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finanzas', '0002_asistencia_cursos'),
    ]

    operations = [
        migrations.AddField(
            model_name='cursos',
            name='choice_field',
            field=models.CharField(blank=True, max_length=50, null=True, choices=[(b'', b'selecciona'), (b'AdminSistema', b'Administrador Sistema'), (b'Admin', b'Administrador'), (b'JefeArea', b'Jefe Area'), (b'Supervisor', b'Supervisor')]),
        ),
    ]
