# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20150223_0744'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='coordinates',
            field=django.contrib.gis.db.models.fields.PointField(srid=4326, null=True),
        ),
    ]
