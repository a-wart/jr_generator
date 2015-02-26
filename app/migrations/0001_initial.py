# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_pgjson.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aircraft',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('_id', models.CharField(default=b'', unique=True, max_length=255, db_index=True)),
                ('code', models.CharField(max_length=3)),
                ('name', django_pgjson.fields.JsonBField()),
                ('weight', django_pgjson.fields.JsonBField()),
                ('lat', models.FloatField(null=True)),
                ('lon', models.FloatField(null=True)),
                ('flightable', models.BooleanField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('place_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='app.Place')),
            ],
            options={
            },
            bases=('app.place',),
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('place_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='app.Place')),
            ],
            options={
            },
            bases=('app.place',),
        ),
        migrations.CreateModel(
            name='Airport',
            fields=[
                ('place_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='app.Place')),
                ('type', models.CharField(max_length=255, choices=[(b'airport', b'airport'), (b'railway', b'railway'), (b'heliport', b'heliport'), (b'bus', b'bus'), (b'harbour', b'harbour'), (b'military', b'military'), (b'seaplane', b'seaplane')])),
            ],
            options={
            },
            bases=('app.place',),
        ),
    ]
