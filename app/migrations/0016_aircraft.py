# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_delete_aircraft'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aircraft',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('_id', models.CharField(default=b'', unique=True, max_length=255, db_index=True)),
                ('name', models.TextField()),
                ('seats', models.IntegerField(null=True)),
                ('wide_body', models.BooleanField(default=False)),
            ],
        ),
    ]
