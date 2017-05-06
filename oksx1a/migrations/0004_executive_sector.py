# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oksx1a', '0003_auto_20161120_0725'),
    ]

    operations = [
        migrations.AddField(
            model_name='executive',
            name='sector',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
