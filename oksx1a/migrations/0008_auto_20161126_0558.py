# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oksx1a', '0007_auto_20161125_2222'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='test',
            name='user',
        ),
        migrations.AddField(
            model_name='test',
            name='testuser',
            field=models.ForeignKey(null=True, to='oksx1a.user'),
        ),
    ]
