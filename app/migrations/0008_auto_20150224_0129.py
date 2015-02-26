# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_place_coordinates'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='place',
            name='lat',
        ),
        migrations.RemoveField(
            model_name='place',
            name='lon',
        ),
    ]
