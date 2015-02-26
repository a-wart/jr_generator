# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_auto_20150225_0016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airline',
            name='address',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='airline',
            name='aviasales_path',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='airline',
            name='description',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='airline',
            name='online_checkin_address',
            field=models.TextField(null=True, blank=True),
        ),
    ]
