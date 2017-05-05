# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oksx1a', '0033_user_average'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='test',
            name='role',
        ),
        migrations.RemoveField(
            model_name='test',
            name='type',
        ),
        migrations.RemoveField(
            model_name='type',
            name='age',
        ),
        migrations.RemoveField(
            model_name='type',
            name='ethnic',
        ),
        migrations.RemoveField(
            model_name='type',
            name='gender',
        ),
    ]
