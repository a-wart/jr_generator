# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_pgjson.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_auto_20150225_0037'),
    ]

    operations = [
        migrations.AddField(
            model_name='airline',
            name='description',
            field=django_pgjson.fields.JsonBField(default={}),
        ),
        migrations.AddField(
            model_name='airline',
            name='name',
            field=django_pgjson.fields.JsonBField(default={}),
        ),
    ]
