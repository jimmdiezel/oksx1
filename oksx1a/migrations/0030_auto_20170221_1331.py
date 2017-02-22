# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oksx1a', '0029_auto_20170221_1013'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.ManyToManyField(to='oksx1a.venue', blank=True, null=True, related_name='useAddress'),
        ),
        migrations.AddField(
            model_name='user',
            name='results',
            field=models.ManyToManyField(to='oksx1a.assessment', blank=True, null=True, related_name='useResults'),
        ),
    ]
