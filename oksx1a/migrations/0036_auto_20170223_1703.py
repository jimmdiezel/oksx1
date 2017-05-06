# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('oksx1a', '0035_auto_20170222_1925'),
    ]

    operations = [
        migrations.CreateModel(
            name='role',
            fields=[
                ('role_no', models.UUIDField(editable=False, serialize=False, primary_key=True, verbose_name='Type Ref:', default=uuid.uuid4)),
                ('dob', models.DateField(blank=True, null=True, verbose_name='Date of Birth')),
                ('race', models.CharField(choices=[('RR', 'Arab'), ('RS', 'Asian'), ('RB', 'Black'), ('RL', 'Latin'), ('RM', 'Mixed'), ('RW', 'White'), ('XO', 'Other'), ('XD', 'Default')], verbose_name='Race', max_length=2, default='XD')),
                ('gender', models.CharField(choices=[('GM', 'Male'), ('GF', 'Female'), ('GT', 'Trans'), ('XO', 'Other'), ('XD', 'Default')], verbose_name='Gender', max_length=2, default='XD')),
                ('status', models.CharField(choices=[('EO', 'Contracted'), ('EA', 'Casual'), ('EE', 'Employed'), ('ET', 'In Training'), ('XD', 'Default')], verbose_name='Employment Status', max_length=2, default='XD')),
                ('authority', models.CharField(choices=[('AA', 'Area'), ('AL', 'Local'), ('AS', 'Supervisor'), ('AW', 'Worker'), ('XD', 'Default')], verbose_name='Authority', max_length=2, default='XD')),
            ],
        ),
        migrations.DeleteModel(
            name='type',
        ),
        migrations.RemoveField(
            model_name='user',
            name='average',
        ),
        migrations.AlterField(
            model_name='network',
            name='website',
            field=models.URLField(blank=True, max_length=75),
        ),
    ]
