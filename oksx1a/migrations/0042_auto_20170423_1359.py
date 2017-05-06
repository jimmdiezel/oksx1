# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oksx1a', '0041_auto_20170305_1607'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='executive',
        ),
        migrations.RemoveField(
            model_name='event',
            name='networks',
        ),
        migrations.RemoveField(
            model_name='event',
            name='photo',
        ),
        migrations.RemoveField(
            model_name='executive',
            name='networks',
        ),
        migrations.RemoveField(
            model_name='location',
            name='company',
        ),
        migrations.RemoveField(
            model_name='location',
            name='networks',
        ),
        migrations.RemoveField(
            model_name='location',
            name='photo',
        ),
        migrations.RemoveField(
            model_name='network',
            name='address',
        ),
        migrations.RemoveField(
            model_name='user',
            name='photo',
        ),
        migrations.AddField(
            model_name='event',
            name='address',
            field=models.ForeignKey(related_name='eveAddress', blank=True, null=True, to='oksx1a.venue'),
        ),
        migrations.AddField(
            model_name='event',
            name='brand',
            field=models.ForeignKey(related_name='eveExec', blank=True, null=True, to='oksx1a.executive'),
        ),
        migrations.AddField(
            model_name='event',
            name='comms',
            field=models.ForeignKey(related_name='eveComms', blank=True, null=True, to='oksx1a.network'),
        ),
        migrations.AddField(
            model_name='event',
            name='photos',
            field=models.ManyToManyField(related_name='evePhotos', blank=True, to='oksx1a.photo'),
        ),
        migrations.AddField(
            model_name='executive',
            name='address',
            field=models.ForeignKey(related_name='exeAddress', blank=True, null=True, to='oksx1a.venue'),
        ),
        migrations.AddField(
            model_name='executive',
            name='comms',
            field=models.ForeignKey(related_name='exeComms', blank=True, null=True, to='oksx1a.network'),
        ),
        migrations.AddField(
            model_name='executive',
            name='photos',
            field=models.ManyToManyField(related_name='exePhotos', blank=True, to='oksx1a.photo'),
        ),
        migrations.AddField(
            model_name='location',
            name='address',
            field=models.ForeignKey(related_name='locAddress', blank=True, null=True, to='oksx1a.venue'),
        ),
        migrations.AddField(
            model_name='location',
            name='brand',
            field=models.ForeignKey(related_name='locExec', blank=True, null=True, to='oksx1a.executive'),
        ),
        migrations.AddField(
            model_name='location',
            name='comms',
            field=models.ForeignKey(related_name='locComms', blank=True, null=True, to='oksx1a.network'),
        ),
        migrations.AddField(
            model_name='location',
            name='photos',
            field=models.ManyToManyField(related_name='locPhotos', blank=True, to='oksx1a.photo'),
        ),
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.ManyToManyField(related_name='useAddress', blank=True, to='oksx1a.venue'),
        ),
        migrations.AddField(
            model_name='user',
            name='logo',
            field=models.ForeignKey(related_name='useLogo', blank=True, null=True, to='oksx1a.photo'),
        ),
        migrations.AddField(
            model_name='user',
            name='photos',
            field=models.ManyToManyField(related_name='usePhotos', blank=True, to='oksx1a.photo'),
        ),
        migrations.AddField(
            model_name='venue',
            name='building',
            field=models.CharField(max_length=2, default='XD', choices=[('VB', 'Boat'), ('VC', 'Construction Site'), ('VF', 'Flat or Apartment'), ('VH', 'House'), ('VO', 'Office'), ('VS', 'Commercial'), ('VU', 'Industrial'), ('XD', 'Default')], verbose_name='Building Type'),
        ),
        migrations.AddField(
            model_name='venue',
            name='country',
            field=models.CharField(max_length=30, blank=True, verbose_name='Country'),
        ),
        migrations.AddField(
            model_name='venue',
            name='premises',
            field=models.CharField(max_length=30, blank=True, verbose_name='Premises'),
        ),
        migrations.AlterField(
            model_name='test',
            name='user',
            field=models.ForeignKey(related_name='tesUser', blank=True, null=True, to='oksx1a.user'),
        ),
    ]
