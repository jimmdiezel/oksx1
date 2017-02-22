# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oksx1a', '0028_auto_20170220_1743'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='address',
        ),
        migrations.RemoveField(
            model_name='executive',
            name='address',
        ),
        migrations.RemoveField(
            model_name='executive',
            name='result',
        ),
        migrations.RemoveField(
            model_name='location',
            name='address',
        ),
        migrations.RemoveField(
            model_name='location',
            name='result',
        ),
        migrations.RemoveField(
            model_name='user',
            name='address',
        ),
        migrations.RemoveField(
            model_name='user',
            name='result',
        ),
    ]
