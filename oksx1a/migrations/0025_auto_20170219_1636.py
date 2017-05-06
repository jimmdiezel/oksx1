# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oksx1a', '0024_auto_20170219_1635'),
    ]

    operations = [
        migrations.RenameField(
            model_name='address',
            old_name='result_no',
            new_name='address_no',
        ),
    ]
