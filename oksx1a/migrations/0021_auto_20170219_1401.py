# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oksx1a', '0020_auto_20170219_1319'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='address',

        ),
    ]
