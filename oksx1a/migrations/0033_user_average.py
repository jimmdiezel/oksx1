# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oksx1a', '0032_auto_20170222_1254'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='average',
            field=models.ForeignKey(null=True, related_name='useResults', blank=True, to='oksx1a.assessment'),
        ),
    ]
