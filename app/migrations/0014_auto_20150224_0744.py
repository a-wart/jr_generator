# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_auto_20150224_0732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flightcode',
            name='aircraft',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
