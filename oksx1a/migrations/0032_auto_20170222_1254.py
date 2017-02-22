# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('oksx1a', '0031_auto_20170222_1206'),
    ]

    operations = [
        migrations.CreateModel(
            name='network',
            fields=[
                ('network_no', models.UUIDField(editable=False, primary_key=True, default=uuid.uuid4, verbose_name='Network Ref:', serialize=False)),
                ('phone', models.CharField(blank=True, max_length=20)),
                ('email', models.EmailField(max_length=200)),
                ('website', models.URLField(max_length=75)),
                ('wifi', models.CharField(blank=True, max_length=225)),
                ('address', models.ManyToManyField(blank=True, to='oksx1a.venue', related_name='useAddress')),
            ],
        ),
        migrations.RemoveField(
            model_name='event',
            name='email',
        ),
        migrations.RemoveField(
            model_name='event',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='event',
            name='website',
        ),
        migrations.RemoveField(
            model_name='executive',
            name='email',
        ),
        migrations.RemoveField(
            model_name='executive',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='executive',
            name='website',
        ),
        migrations.RemoveField(
            model_name='location',
            name='email',
        ),
        migrations.RemoveField(
            model_name='location',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='location',
            name='website',
        ),
        migrations.RemoveField(
            model_name='location',
            name='wifi',
        ),
        migrations.RemoveField(
            model_name='user',
            name='address',
        ),
        migrations.RemoveField(
            model_name='user',
            name='age',
        ),
        migrations.RemoveField(
            model_name='user',
            name='email',
        ),
        migrations.RemoveField(
            model_name='user',
            name='ethnic',
        ),
        migrations.RemoveField(
            model_name='user',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='user',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='user',
            name='results',
        ),

    ]
