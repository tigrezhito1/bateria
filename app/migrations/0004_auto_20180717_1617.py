# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-07-17 16:17
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20180717_1556'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vehiculo',
            old_name='anio',
            new_name='marca',
        ),
        migrations.RemoveField(
            model_name='produccion',
            name='vehiculo',
        ),
        migrations.RemoveField(
            model_name='vehiculo',
            name='color',
        ),
        migrations.RemoveField(
            model_name='vehiculo',
            name='kms',
        ),
        migrations.RemoveField(
            model_name='vehiculo',
            name='marca_v',
        ),
        migrations.RemoveField(
            model_name='vehiculo',
            name='modelo_v',
        ),
        migrations.RemoveField(
            model_name='vehiculo',
            name='motor',
        ),
        migrations.RemoveField(
            model_name='vehiculo',
            name='placa',
        ),
        migrations.RemoveField(
            model_name='vehiculo',
            name='serie',
        ),
        migrations.AddField(
            model_name='produccion',
            name='marca_vehiculo',
            field=models.ForeignKey(blank=True, help_text='Marca del veh\xedculo (p.e. Nissan)', max_length=1000, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Vehiculo'),
        ),
        migrations.AlterField(
            model_name='produccion',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2018, 7, 17, 16, 17, 12, 81432), editable=False, help_text='Fecha de recepci\xf3n de la llamada (No se puede modificar)'),
        ),
    ]
