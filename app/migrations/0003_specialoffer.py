# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20150223_0524'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpecialOffer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.TextField()),
                ('_id', models.CharField(default=b'', unique=True, max_length=255, db_index=True)),
                ('airline_mongo_id', models.CharField(default=b'', max_length=255, db_index=True)),
                ('start_date', models.DateTimeField()),
                ('finish_date', models.DateTimeField()),
                ('flight_start_date', models.DateTimeField()),
                ('flight_finish_date', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
