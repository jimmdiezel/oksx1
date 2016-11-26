# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oksx1a', '0006_auto_20161125_2159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='user',
            field=models.ForeignKey(default=0, to='oksx1a.user'),
        ),
    ]
