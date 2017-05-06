# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oksx1a', '0010_auto_20161204_1023'),
    ]

    operations = [
        migrations.RenameField(
            model_name='location',
            old_name='administration',
            new_name='company',
        ),
        migrations.AlterField(
            model_name='location',
            name='add1',
            field=models.CharField(max_length=80, verbose_name='Building'),
        ),
    ]
