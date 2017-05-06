# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oksx1a', '0022_auto_20170219_1410'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='address',
            field=models.ForeignKey(null=True, related_name='eveAddress', blank=True, to='oksx1a.address'),
        ),
    ]
