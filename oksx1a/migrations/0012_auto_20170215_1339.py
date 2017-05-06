# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oksx1a', '0011_auto_20161205_2237'),
    ]

    operations = [
        migrations.RenameField(
            model_name='test',
            old_name='testuser',
            new_name='user',
        ),
    ]
