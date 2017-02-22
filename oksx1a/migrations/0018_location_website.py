# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oksx1a', '0017_auto_20170216_1824'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='website',
            field=models.URLField(max_length=80, blank=True),
        ),
    ]
