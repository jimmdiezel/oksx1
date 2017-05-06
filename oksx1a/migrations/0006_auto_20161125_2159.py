# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oksx1a', '0005_auto_20161120_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='role',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='test',
            name='type',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='test',
            name='user',
            field=models.ForeignKey(to='oksx1a.user', blank=True, null=True),
        ),
    ]
