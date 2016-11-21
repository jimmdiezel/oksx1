# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oksx1a', '0002_auto_20161120_0702'),
    ]

    operations = [
        migrations.RenameField(
            model_name='location',
            old_name='executive',
            new_name='exec',
        ),
    ]
