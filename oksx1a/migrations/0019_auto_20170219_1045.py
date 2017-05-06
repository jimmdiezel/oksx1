# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oksx1a', '0018_location_website'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='add1',
            field=models.CharField(max_length=80, verbose_name='Site'),
        ),
    ]
