# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oksx1a', '0021_auto_20170219_1401'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='postcode',
        ),
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.ForeignKey(blank=True, related_name='useAddress', to='oksx1a.address', null=True),
        ),
    ]
