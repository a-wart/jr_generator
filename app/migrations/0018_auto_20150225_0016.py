# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_airline'),
    ]

    operations = [
        migrations.RenameField(
            model_name='airline',
            old_name='alliance_id',
            new_name='alliance_mongo_id',
        ),
    ]
