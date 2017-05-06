# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oksx1a', '0013_auto_20170215_1622'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='executive',
            name='director',
        ),
    ]
