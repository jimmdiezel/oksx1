# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oksx1a', '0034_auto_20170222_1621'),
    ]

    operations = [
        migrations.AddField(
            model_name='type',
            name='authority',
            field=models.CharField(max_length=2, default='XD', choices=[('AA', 'Area'), ('AL', 'Local'), ('AS', 'Supervisor'), ('AW', 'Worker'), ('XD', 'Default')], verbose_name='Gender'),
        ),
        migrations.AddField(
            model_name='type',
            name='dob',
            field=models.DateField(blank=True, null=True, verbose_name='Date of Birth'),
        ),
        migrations.AddField(
            model_name='type',
            name='gender',
            field=models.CharField(max_length=2, default='XD', choices=[('GM', 'Male'), ('GF', 'Female'), ('GT', 'Trans'), ('XO', 'Other'), ('XD', 'Default')], verbose_name='Gender'),
        ),
        migrations.AddField(
            model_name='type',
            name='race',
            field=models.CharField(max_length=2, default='XD', choices=[('RR', 'Arab'), ('RS', 'Asian'), ('RB', 'Black'), ('RL', 'Latin'), ('RM', 'Mixed'), ('RW', 'White'), ('XO', 'Other'), ('XD', 'Default')], verbose_name='Race'),
        ),
        migrations.AddField(
            model_name='type',
            name='status',
            field=models.CharField(max_length=2, default='XD', choices=[('EO', 'Contracted'), ('EA', 'Casual'), ('EE', 'Employed'), ('ET', 'In Training'), ('XD', 'Default')], verbose_name='Employment Status'),
        ),
    ]
