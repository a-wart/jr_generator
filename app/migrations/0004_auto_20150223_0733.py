# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.postgres.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_specialoffer'),
    ]

    operations = [
        migrations.AddField(
            model_name='specialoffer',
            name='archive',
            field=django.contrib.postgres.fields.ArrayField(null=True, base_field=models.CharField(max_length=255), size=None),
        ),
        migrations.AddField(
            model_name='specialoffer',
            name='description',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='specialoffer',
            name='external_url',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='specialoffer',
            name='host',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='specialoffer',
            name='price',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='specialoffer',
            name='slug_cache',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
    ]
