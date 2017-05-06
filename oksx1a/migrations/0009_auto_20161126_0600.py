# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oksx1a', '0008_auto_20161126_0558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='testuser',
            field=models.ForeignKey(blank=True, to='oksx1a.user', null=True),
        ),
    ]
