# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oksx1a', '0042_auto_20170423_1359'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='logo',
        ),
        migrations.RemoveField(
            model_name='executive',
            name='logo',
        ),
        migrations.RemoveField(
            model_name='location',
            name='logo',
        ),
    ]
