# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oksx1a', '0038_user_roles'),
    ]

    operations = [
        migrations.RenameField(
            model_name='location',
            old_name='network',
            new_name='networks',
        ),
        migrations.RemoveField(
            model_name='event',
            name='contact1',
        ),
        migrations.RemoveField(
            model_name='event',
            name='contact2',
        ),
        migrations.RemoveField(
            model_name='executive',
            name='contact1',
        ),
        migrations.RemoveField(
            model_name='executive',
            name='contact2',
        ),
        migrations.RemoveField(
            model_name='location',
            name='contact1',
        ),
        migrations.RemoveField(
            model_name='location',
            name='contact2',
        ),
        migrations.RemoveField(
            model_name='location',
            name='steward1',
        ),
        migrations.RemoveField(
            model_name='location',
            name='steward2',
        ),
        migrations.RemoveField(
            model_name='location',
            name='steward3',
        ),
        migrations.RemoveField(
            model_name='location',
            name='steward4',
        ),
        migrations.AddField(
            model_name='event',
            name='contacts',
            field=models.ManyToManyField(to='oksx1a.user', blank=True, related_name='eveContacts', null=True),
        ),
        migrations.AddField(
            model_name='executive',
            name='contacts',
            field=models.ManyToManyField(to='oksx1a.user', blank=True, related_name='exeContacts', null=True),
        ),
        migrations.AddField(
            model_name='executive',
            name='networks',
            field=models.ForeignKey(blank=True, related_name='exeNetwork', to='oksx1a.network', null=True),
        ),
        migrations.AddField(
            model_name='executive',
            name='stewards',
            field=models.ManyToManyField(to='oksx1a.user', blank=True, related_name='exeStewards', null=True),
        ),
        migrations.AddField(
            model_name='location',
            name='contacts',
            field=models.ManyToManyField(to='oksx1a.user', blank=True, related_name='locContacts', null=True),
        ),
        migrations.AddField(
            model_name='location',
            name='stewards',
            field=models.ManyToManyField(to='oksx1a.user', blank=True, related_name='locStewards', null=True),
        ),
    ]
