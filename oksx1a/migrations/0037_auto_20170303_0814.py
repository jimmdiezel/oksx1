# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('oksx1a', '0036_auto_20170223_1703'),
    ]

    operations = [
        migrations.CreateModel(
            name='photo',
            fields=[
                ('timestamp', models.DateTimeField(auto_now_add=True, null=True)),
                ('photo_no', models.UUIDField(editable=False, verbose_name='Photo Ref:', serialize=False, primary_key=True, default=uuid.uuid4)),
                ('photo', models.ImageField(blank=True, upload_to='', max_length=150)),
            ],
        ),
        migrations.RemoveField(
            model_name='test',
            name='avg_hours',
        ),
        migrations.RemoveField(
            model_name='test',
            name='received',
        ),
        migrations.RemoveField(
            model_name='test',
            name='start',
        ),
        migrations.AddField(
            model_name='assessment',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='location',
            name='network',
            field=models.ForeignKey(null=True, blank=True, related_name='locNetwork', to='oksx1a.network'),
        ),
        migrations.AddField(
            model_name='network',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='role',
            name='avg_hours',
            field=models.DurationField(null=True, verbose_name='Average Weekly Hours'),
        ),
        migrations.AddField(
            model_name='role',
            name='start',
            field=models.DateField(null=True, verbose_name='Start of Service'),
        ),
        migrations.AddField(
            model_name='role',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='test',
            name='roles',
            field=models.ForeignKey(null=True, blank=True, related_name='tesRoles', to='oksx1a.role'),
        ),
        migrations.AddField(
            model_name='user',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='venue',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
