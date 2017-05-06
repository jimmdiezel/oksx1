# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oksx1a', '0044_auto_20170423_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='comms',
            field=models.ForeignKey(null=True, verbose_name='Network', blank=True, related_name='eveComms', to='oksx1a.network'),
        ),
        migrations.AlterField(
            model_name='event',
            name='photos',
            field=models.ManyToManyField(to='oksx1a.photo', related_name='evePhotos', blank=True),
        ),
        migrations.AlterField(
            model_name='executive',
            name='comms',
            field=models.ForeignKey(null=True, verbose_name='Network', blank=True, related_name='exeComms', to='oksx1a.network'),
        ),
        migrations.AlterField(
            model_name='executive',
            name='photos',
            field=models.ManyToManyField(to='oksx1a.photo', related_name='exePhotos', blank=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='comms',
            field=models.ForeignKey(null=True, verbose_name='Network', blank=True, related_name='locComms', to='oksx1a.network'),
        ),
        migrations.AlterField(
            model_name='location',
            name='photos',
            field=models.ManyToManyField(to='oksx1a.photo', related_name='locPhotos', blank=True),
        ),
    ]
