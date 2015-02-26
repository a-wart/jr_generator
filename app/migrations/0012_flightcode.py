# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.postgres.fields
import django_pgjson.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20150224_0259'),
    ]

    operations = [
        migrations.CreateModel(
            name='FlightCode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('_id', models.CharField(default=b'', unique=True, max_length=255, db_index=True)),
                ('aircraft_mongo_ids', django.contrib.postgres.fields.ArrayField(null=True, base_field=models.CharField(max_length=255), size=None)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
                ('first_date', models.DateTimeField()),
                ('last_date', models.DateTimeField()),
                ('airline_mongo_id', models.CharField(max_length=255)),
                ('flight_number', models.CharField(max_length=255)),
                ('aircraft', models.CharField(max_length=255)),
                ('airport_route_mongo_id', models.CharField(max_length=255)),
                ('weight', django_pgjson.fields.JsonBField()),
                ('durations', django.contrib.postgres.fields.ArrayField(null=True, base_field=models.IntegerField(), size=None)),
                ('duration', models.IntegerField(null=True)),
            ],
        ),
    ]
