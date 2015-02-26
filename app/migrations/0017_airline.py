# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.postgres.fields
import django_pgjson.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_aircraft'),
    ]

    operations = [
        migrations.CreateModel(
            name='Airline',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('_id', models.CharField(default=b'', unique=True, max_length=255, db_index=True)),
                ('main_color', models.CharField(max_length=255, null=True)),
                ('additional_color', models.CharField(max_length=255, null=True)),
                ('name', models.CharField(max_length=255, null=True)),
                ('phone_number', models.CharField(max_length=255, null=True)),
                ('website_address', models.CharField(max_length=255, null=True)),
                ('address', models.TextField()),
                ('pending_destroy', models.BooleanField(default=False)),
                ('online_checkin_address', models.TextField()),
                ('description', models.TextField()),
                ('aviasales_path', models.TextField()),
                ('code', models.CharField(max_length=2)),
                ('alliance_id', models.CharField(max_length=255, null=True)),
                ('created_at', models.DateTimeField(null=True)),
                ('updated_at', models.DateTimeField(null=True)),
                ('iata_name', django.contrib.postgres.fields.ArrayField(null=True, base_field=models.CharField(max_length=255), size=None)),
                ('pending_iata_name', django.contrib.postgres.fields.ArrayField(null=True, base_field=models.CharField(max_length=255), size=None)),
                ('weight', django_pgjson.fields.JsonBField()),
            ],
        ),
    ]
