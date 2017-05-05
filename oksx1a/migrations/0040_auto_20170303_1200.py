# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oksx1a', '0039_auto_20170303_1153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='contacts',
            field=models.ManyToManyField(related_name='eveContacts', to='oksx1a.user', blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='end',
            field=models.DateTimeField(null=True, verbose_name='End', blank=True),
        ),
        migrations.AlterField(
            model_name='executive',
            name='contacts',
            field=models.ManyToManyField(related_name='exeContacts', to='oksx1a.user', blank=True),
        ),
        migrations.AlterField(
            model_name='executive',
            name='stewards',
            field=models.ManyToManyField(related_name='exeStewards', to='oksx1a.user', blank=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='contacts',
            field=models.ManyToManyField(related_name='locContacts', to='oksx1a.user', blank=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='stewards',
            field=models.ManyToManyField(related_name='locStewards', to='oksx1a.user', blank=True),
        ),
    ]
