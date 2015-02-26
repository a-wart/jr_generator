# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20150224_0239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='route',
            name='created_at',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='route',
            name='updated_at',
            field=models.DateTimeField(),
        ),
    ]
