# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oksx1a', '0015_auto_20170216_1813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
