# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oksx1a', '0016_auto_20170216_1818'),
    ]

    operations = [
        migrations.AddField(
            model_name='executive',
            name='director',
            field=models.ForeignKey(null=True, blank=True, verbose_name='Director', to='oksx1a.user'),
        ),
        migrations.AddField(
            model_name='location',
            name='manager',
            field=models.ForeignKey(null=True, blank=True, verbose_name='General Manager', to='oksx1a.user'),
        ),
        migrations.AddField(
            model_name='location',
            name='steward1',
            field=models.ForeignKey(related_name='locSteward1', null=True, blank=True, verbose_name='Steward 1', to='oksx1a.user'),
        ),
        migrations.AddField(
            model_name='location',
            name='steward2',
            field=models.ForeignKey(related_name='locSteward2', null=True, blank=True, verbose_name='Steward 2', to='oksx1a.user'),
        ),
        migrations.AddField(
            model_name='location',
            name='steward3',
            field=models.ForeignKey(related_name='locSteward3', null=True, blank=True, verbose_name='Steward 3', to='oksx1a.user'),
        ),
        migrations.AddField(
            model_name='location',
            name='steward4',
            field=models.ForeignKey(related_name='locSteward4', null=True, blank=True, verbose_name='Steward 4', to='oksx1a.user'),
        ),
    ]
