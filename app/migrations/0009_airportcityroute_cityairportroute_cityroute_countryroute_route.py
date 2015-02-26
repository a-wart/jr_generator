# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.postgres.fields
import django_pgjson.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20150224_0129'),
    ]

    operations = [
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('_id', models.CharField(default=b'', unique=True, max_length=255, db_index=True)),
                ('airline_mongo_ids', django.contrib.postgres.fields.ArrayField(null=True, base_field=models.CharField(max_length=255), size=None)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('dest_mongo_id', models.CharField(max_length=255)),
                ('orig_mongo_id', models.CharField(max_length=255)),
                ('max_duration', models.IntegerField(null=True)),
                ('min_duration', models.IntegerField(null=True)),
                ('weight', django_pgjson.fields.JsonBField()),
            ],
        ),
        migrations.CreateModel(
            name='AirportCityRoute',
            fields=[
                ('route_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='app.Route')),
            ],
            bases=('app.route',),
        ),
        migrations.CreateModel(
            name='CityAirportRoute',
            fields=[
                ('route_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='app.Route')),
            ],
            bases=('app.route',),
        ),
        migrations.CreateModel(
            name='CityRoute',
            fields=[
                ('route_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='app.Route')),
                ('aviasales_path', models.TextField()),
            ],
            bases=('app.route',),
        ),
        migrations.CreateModel(
            name='CountryRoute',
            fields=[
                ('route_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='app.Route')),
            ],
            bases=('app.route',),
        ),
    ]
