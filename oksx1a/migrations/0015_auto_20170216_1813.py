# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oksx1a', '0014_remove_executive_director'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='manager',
        ),
        migrations.RemoveField(
            model_name='location',
            name='steward1',
        ),
        migrations.RemoveField(
            model_name='location',
            name='steward2',
        ),
        migrations.RemoveField(
            model_name='location',
            name='steward3',
        ),
        migrations.RemoveField(
            model_name='location',
            name='steward4',
        ),
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.IntegerField(default=0),
        ),
    ]
