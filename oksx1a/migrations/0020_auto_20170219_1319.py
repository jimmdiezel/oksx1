# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('oksx1a', '0019_auto_20170219_1045'),
    ]

    operations = [
        migrations.CreateModel(
            name='address',
            fields=[
                ('address_no', models.UUIDField(serialize=False, default=uuid.uuid4, editable=False, verbose_name='Test No', primary_key=True)),
                ('add1', models.CharField(max_length=80, verbose_name='Address Line 1')),
                ('add2', models.CharField(max_length=80, blank=True, verbose_name='Address Line 2')),
                ('add3', models.CharField(max_length=80, blank=True, verbose_name='Address Line 3')),
                ('add4', models.CharField(max_length=80, blank=True, verbose_name='Address Line 4')),
                ('add5', models.CharField(max_length=80, blank=True, verbose_name='Address Line 5')),
                ('postcode', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='results',
            fields=[
                ('result_no', models.UUIDField(serialize=False, default=uuid.uuid4, editable=False, verbose_name='Test No', primary_key=True)),
                ('t1', models.IntegerField(default=0)),
                ('t2', models.IntegerField(default=0)),
                ('t3', models.IntegerField(default=0)),
                ('t4', models.IntegerField(default=0)),
                ('t5', models.IntegerField(default=0)),
                ('t6', models.IntegerField(default=0)),
                ('t7', models.IntegerField(default=0)),
                ('t8', models.IntegerField(default=0)),
                ('t9', models.IntegerField(default=0)),
                ('t10', models.IntegerField(default=0)),
                ('t11', models.IntegerField(default=0)),
                ('t12', models.IntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='event',
            name='add1',
        ),
        migrations.RemoveField(
            model_name='event',
            name='add2',
        ),
        migrations.RemoveField(
            model_name='event',
            name='add3',
        ),
        migrations.RemoveField(
            model_name='event',
            name='add4',
        ),
        migrations.RemoveField(
            model_name='event',
            name='add5',
        ),
        migrations.RemoveField(
            model_name='event',
            name='postcode',
        ),
        migrations.RemoveField(
            model_name='location',
            name='add1',
        ),
        migrations.RemoveField(
            model_name='location',
            name='add2',
        ),
        migrations.RemoveField(
            model_name='location',
            name='add3',
        ),
        migrations.RemoveField(
            model_name='location',
            name='add4',
        ),
        migrations.RemoveField(
            model_name='location',
            name='add5',
        ),
        migrations.RemoveField(
            model_name='location',
            name='postcode',
        ),
        migrations.RemoveField(
            model_name='test',
            name='t1',
        ),
        migrations.RemoveField(
            model_name='test',
            name='t10',
        ),
        migrations.RemoveField(
            model_name='test',
            name='t11',
        ),
        migrations.RemoveField(
            model_name='test',
            name='t12',
        ),
        migrations.RemoveField(
            model_name='test',
            name='t2',
        ),
        migrations.RemoveField(
            model_name='test',
            name='t3',
        ),
        migrations.RemoveField(
            model_name='test',
            name='t4',
        ),
        migrations.RemoveField(
            model_name='test',
            name='t5',
        ),
        migrations.RemoveField(
            model_name='test',
            name='t6',
        ),
        migrations.RemoveField(
            model_name='test',
            name='t7',
        ),
        migrations.RemoveField(
            model_name='test',
            name='t8',
        ),
        migrations.RemoveField(
            model_name='test',
            name='t9',
        ),        migrations.AddField(
            model_name='executive',
            name='address',
            field=models.ForeignKey(to='oksx1a.address', blank=True, null=True, related_name='exeAddress'),
        ),
        migrations.AddField(
            model_name='executive',
            name='result',
            field=models.ForeignKey(to='oksx1a.results', blank=True, null=True, related_name='exeResult'),
        ),
        migrations.AddField(
            model_name='location',
            name='address',
            field=models.ForeignKey(to='oksx1a.address', blank=True, null=True, related_name='locAddress'),
        ),
        migrations.AddField(
            model_name='location',
            name='result',
            field=models.ForeignKey(to='oksx1a.results', blank=True, null=True, related_name='locResult'),
        ),
        migrations.AddField(
            model_name='test',
            name='result',
            field=models.ForeignKey(to='oksx1a.results', blank=True, null=True, related_name='tesResult'),
        ),
        migrations.AddField(
            model_name='user',
            name='result',
            field=models.ForeignKey(to='oksx1a.results', blank=True, null=True, related_name='useResult'),
        ),
    ]
