# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_specialoffer_expired'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specialoffer',
            name='finish_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='specialoffer',
            name='flight_finish_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='specialoffer',
            name='flight_start_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='specialoffer',
            name='start_date',
            field=models.DateTimeField(null=True),
        ),
    ]
