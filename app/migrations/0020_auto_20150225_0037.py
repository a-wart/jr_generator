# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_auto_20150225_0019'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='airline',
            name='description',
        ),
        migrations.RemoveField(
            model_name='airline',
            name='name',
        ),
    ]
