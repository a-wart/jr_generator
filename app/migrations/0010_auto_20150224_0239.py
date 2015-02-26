# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_airportcityroute_cityairportroute_cityroute_countryroute_route'),
    ]

    operations = [
        migrations.AlterField(
            model_name='route',
            name='max_duration',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='route',
            name='min_duration',
            field=models.BigIntegerField(null=True),
        ),
    ]
