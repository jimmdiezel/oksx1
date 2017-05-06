# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oksx1a', '0012_auto_20170215_1339'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='contact',
        ),
        migrations.RemoveField(
            model_name='executive',
            name='contact',
        ),
        migrations.RemoveField(
            model_name='location',
            name='contact',
        ),
        migrations.AddField(
            model_name='event',
            name='contact1',
            field=models.ForeignKey(related_name='eveContact1', to='oksx1a.user', null=True, verbose_name='Contact 1', blank=True),
        ),
        migrations.AddField(
            model_name='event',
            name='contact2',
            field=models.ForeignKey(related_name='eveContact2', to='oksx1a.user', null=True, verbose_name='Contact 2', blank=True),
        ),
        migrations.AddField(
            model_name='executive',
            name='contact1',
            field=models.ForeignKey(related_name='exeContact1', to='oksx1a.user', null=True, verbose_name='Contact 1', blank=True),
        ),
        migrations.AddField(
            model_name='executive',
            name='contact2',
            field=models.ForeignKey(related_name='exeContact2', to='oksx1a.user', null=True, verbose_name='Contact 2', blank=True),
        ),
        migrations.AddField(
            model_name='location',
            name='contact1',
            field=models.ForeignKey(related_name='locContact1', to='oksx1a.user', null=True, verbose_name='Contact 1', blank=True),
        ),
        migrations.AddField(
            model_name='location',
            name='contact2',
            field=models.ForeignKey(related_name='locContact2', to='oksx1a.user', null=True, verbose_name='Contact 2', blank=True),
        ),
        ]
