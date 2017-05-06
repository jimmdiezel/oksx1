# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oksx1a', '0040_auto_20170303_1200'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='roles',
        ),
        migrations.AddField(
            model_name='event',
            name='networks',
            field=models.ForeignKey(to='oksx1a.network', null=True, related_name='eveNetwork', blank=True),
        ),
    ]
