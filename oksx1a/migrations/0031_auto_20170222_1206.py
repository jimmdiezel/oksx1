# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('oksx1a', '0030_auto_20170221_1331'),
    ]

    operations = [
        migrations.CreateModel(
            name='type',
            fields=[
                ('type_no', models.UUIDField(verbose_name='Type Ref:', editable=False, default=uuid.uuid4, primary_key=True, serialize=False)),
                ('age', models.IntegerField(blank=True, default=0)),
                ('gender', models.IntegerField(blank=True, default=0)),
                ('ethnic', models.IntegerField(verbose_name='Ethnic Background', blank=True, default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='test',
            name='testno',
        ),
        migrations.AddField(
            model_name='test',
            name='test_no',
            field=models.UUIDField(verbose_name='Test Ref:', editable=False, default=uuid.uuid4, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='assessment_no',
            field=models.UUIDField(verbose_name='Assessment Ref:', editable=False, default=uuid.uuid4, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='address',
            field=models.ManyToManyField(blank=True, related_name='useAddress', to='oksx1a.venue'),
        ),
        migrations.AlterField(
            model_name='user',
            name='results',
            field=models.ManyToManyField(blank=True, related_name='useResults', to='oksx1a.assessment'),
        ),
        migrations.AlterField(
            model_name='venue',
            name='venue_no',
            field=models.UUIDField(verbose_name='Venue Ref:', editable=False, default=uuid.uuid4, primary_key=True, serialize=False),
        ),
    ]
