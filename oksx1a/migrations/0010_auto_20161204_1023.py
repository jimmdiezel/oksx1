# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oksx1a', '0009_auto_20161126_0600'),
    ]

    operations = [
        migrations.RenameField(
            model_name='location',
            old_name='exec',
            new_name='administration',
        ),
        migrations.AlterField(
            model_name='location',
            name='add1',
            field=models.CharField(max_length=80, verbose_name='Name/Number'),
        ),
        migrations.AlterField(
            model_name='location',
            name='add2',
            field=models.CharField(max_length=80, blank=True, verbose_name='Street'),
        ),
        migrations.AlterField(
            model_name='location',
            name='add3',
            field=models.CharField(max_length=80, blank=True, verbose_name='Town/City'),
        ),
        migrations.AlterField(
            model_name='location',
            name='add4',
            field=models.CharField(max_length=80, blank=True, verbose_name='Region'),
        ),
        migrations.AlterField(
            model_name='location',
            name='add5',
            field=models.CharField(max_length=80, blank=True, verbose_name='Country'),
        ),
    ]
