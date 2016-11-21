# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oksx1a', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='user',
            field=models.ForeignKey(blank=True, to='oksx1a.user'),
        ),
        migrations.AlterField(
            model_name='user',
            name='ethnic',
            field=models.IntegerField(blank=True, verbose_name='Ethnic Background', default=0),
        ),
    ]
