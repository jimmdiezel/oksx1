# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oksx1a', '0037_auto_20170303_0814'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='roles',
            field=models.OneToOneField(to='oksx1a.role', blank=True, null=True),
        ),
    ]
