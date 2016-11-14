# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('description', models.TextField(blank=True, max_length=600)),
                ('add1', models.CharField(max_length=80, verbose_name='Address Line 1')),
                ('add2', models.CharField(blank=True, max_length=80, verbose_name='Address Line 2')),
                ('add3', models.CharField(blank=True, max_length=80, verbose_name='Address Line 3')),
                ('add4', models.CharField(blank=True, max_length=80, verbose_name='Address Line 4')),
                ('add5', models.CharField(blank=True, max_length=80, verbose_name='Address Line 5')),
                ('postcode', models.CharField(max_length=10)),
                ('start', models.DateTimeField(verbose_name='Beginning')),
                ('end', models.DateTimeField(blank=True, verbose_name='End')),
                ('logo', models.ImageField(blank=True, max_length=150, upload_to='')),
                ('photo', models.ImageField(blank=True, upload_to='')),
                ('contact', models.CharField(blank=True, max_length=60, verbose_name='Contact Name')),
                ('email', models.EmailField(max_length=200)),
                ('phone', models.IntegerField()),
                ('website', models.URLField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='executive',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('director', models.CharField(blank=True, max_length=60, verbose_name='Company Director')),
                ('contact', models.CharField(blank=True, max_length=60, verbose_name='Contact Name')),
                ('email', models.EmailField(blank=True, max_length=200)),
                ('phone', models.IntegerField(default=0)),
                ('website', models.URLField(max_length=50)),
                ('logo', models.ImageField(blank=True, max_length=150, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('add1', models.CharField(max_length=80, verbose_name='Address Line 1')),
                ('add2', models.CharField(blank=True, max_length=80, verbose_name='Address Line 2')),
                ('add3', models.CharField(blank=True, max_length=80, verbose_name='Address Line 3')),
                ('add4', models.CharField(blank=True, max_length=80, verbose_name='Address Line 4')),
                ('add5', models.CharField(blank=True, max_length=80, verbose_name='Address Line 5')),
                ('postcode', models.CharField(max_length=10)),
                ('contact', models.CharField(blank=True, max_length=60)),
                ('email', models.EmailField(blank=True, max_length=200)),
                ('phone', models.IntegerField(default=0, blank=True)),
                ('steward1', models.CharField(blank=True, max_length=60)),
                ('steward2', models.CharField(blank=True, max_length=60)),
                ('steward3', models.CharField(blank=True, max_length=60)),
                ('steward4', models.CharField(blank=True, max_length=60)),
                ('manager', models.CharField(blank=True, max_length=60, verbose_name='General Manager')),
                ('wifi', models.CharField(blank=True, max_length=40)),
                ('logo', models.ImageField(blank=True, max_length=150, upload_to='')),
                ('photo', models.ImageField(blank=True, max_length=150, upload_to='')),
                ('executive', models.ForeignKey(to='oksx1a.executive')),
            ],
        ),
        migrations.CreateModel(
            name='test',
            fields=[
                ('testno', models.UUIDField(default=uuid.uuid4, serialize=False, verbose_name='Test No', primary_key=True, editable=False)),
                ('pik', models.CharField(max_length=10, verbose_name='Personal ID Key')),
                ('role', models.IntegerField(default=0)),
                ('type', models.IntegerField(default=0)),
                ('start', models.DateTimeField(verbose_name='Start of Service')),
                ('avg_hours', models.DurationField(verbose_name='Average Weekly Hours')),
                ('received', models.DateTimeField(verbose_name='Time/Date Stamp')),
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
                ('location', models.ForeignKey(to='oksx1a.location')),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='First Name(s)')),
                ('last_name', models.CharField(max_length=30, verbose_name='Last Name')),
                ('username', models.CharField(max_length=30, verbose_name='User Name')),
                ('union', models.CharField(blank=True, max_length=30)),
                ('union_no', models.CharField(blank=True, max_length=30)),
                ('age', models.IntegerField(default=0)),
                ('ethnic', models.IntegerField(default=0, verbose_name='Ethnic Background')),
                ('address', models.TextField(blank=True, max_length=320)),
                ('postcode', models.CharField(blank=True, max_length=10)),
                ('phone', models.IntegerField(default=0, blank=True)),
                ('email', models.EmailField(max_length=200)),
                ('photo', models.ImageField(blank=True, max_length=150, upload_to='')),
            ],
        ),
        migrations.AddField(
            model_name='test',
            name='user',
            field=models.ForeignKey(to='oksx1a.user'),
        ),
        migrations.AddField(
            model_name='event',
            name='executive',
            field=models.ForeignKey(to='oksx1a.executive'),
        ),
    ]
