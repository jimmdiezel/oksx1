# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('oksx1a', '0025_auto_20170219_1636'),
    ]

    operations = [
        migrations.CreateModel(
            name='venue',
            fields=[
                ('venue_no', models.UUIDField(serialize=False, verbose_name='Address No', default=uuid.uuid4, editable=False, primary_key=True)),
                ('add1', models.CharField(verbose_name='Address Line 1', max_length=80, default='Unknown')),
                ('add2', models.CharField(verbose_name='Address Line 2', max_length=80, blank=True)),
                ('add3', models.CharField(verbose_name='Address Line 3', max_length=80, blank=True)),
                ('add4', models.CharField(verbose_name='Address Line 4', max_length=80, blank=True)),
                ('add5', models.CharField(verbose_name='Address Line 5', max_length=80, blank=True)),
                ('postcode', models.CharField(max_length=10)),
            ],
        ),
        migrations.AlterField(
            model_name='event',
            name='address',
            field=models.ForeignKey(blank=True, related_name='eveVenue', to='oksx1a.venue', null=True),
        ),
        migrations.AlterField(
            model_name='executive',
            name='address',
            field=models.ForeignKey(blank=True, related_name='exeVenue', to='oksx1a.venue', null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='address',
            field=models.ForeignKey(blank=True, related_name='locVenue', to='oksx1a.venue', null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='address',
            field=models.ForeignKey(blank=True, related_name='useVenue', to='oksx1a.venue', null=True),
        ),
        migrations.DeleteModel(
            name='address',
        ),
    ]
