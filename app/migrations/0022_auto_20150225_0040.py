# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_auto_20150225_0038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airline',
            name='code',
            field=models.CharField(max_length=3),
        ),
    ]
