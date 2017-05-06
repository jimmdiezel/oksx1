# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oksx1a', '0004_executive_sector'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='start',
            field=models.DateField(verbose_name='Start of Service'),
        ),
    ]
