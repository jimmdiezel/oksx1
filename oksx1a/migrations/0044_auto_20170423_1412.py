# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oksx1a', '0043_auto_20170423_1409'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='logo',
            field=models.ForeignKey(blank=True, related_name='eveLogo', to='oksx1a.photo', null=True),
        ),
        migrations.AddField(
            model_name='executive',
            name='logo',
            field=models.ForeignKey(blank=True, related_name='exeLogo', to='oksx1a.photo', null=True),
        ),
        migrations.AddField(
            model_name='location',
            name='logo',
            field=models.ForeignKey(blank=True, related_name='locLogo', to='oksx1a.photo', null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='photos',
            field=models.ManyToManyField(related_name='evePhotos', to='oksx1a.photo', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='executive',
            name='photos',
            field=models.ManyToManyField(related_name='exePhotos', to='oksx1a.photo', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='photos',
            field=models.ManyToManyField(related_name='locPhotos', to='oksx1a.photo', null=True, blank=True),
        ),
    ]
