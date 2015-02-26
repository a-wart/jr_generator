# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_flightcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flightcode',
            name='created_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='flightcode',
            name='first_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='flightcode',
            name='last_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='flightcode',
            name='updated_at',
            field=models.DateTimeField(null=True),
        ),
    ]
