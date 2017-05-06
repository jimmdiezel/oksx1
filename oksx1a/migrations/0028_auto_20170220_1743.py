# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('oksx1a', '0027_auto_20170219_1707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assessment',
            name='assessment_no',
            field=models.UUIDField(verbose_name='Assessment No', serialize=False, default=uuid.uuid4, primary_key=True, editable=False),
        ),
        migrations.AlterField(
            model_name='venue',
            name='add1',
            field=models.CharField(blank=True, verbose_name='Address Line 1', max_length=80),
        ),
        migrations.AlterField(
            model_name='venue',
            name='venue_no',
            field=models.UUIDField(verbose_name='Venue No', serialize=False, default=uuid.uuid4, primary_key=True, editable=False),
        ),
    ]
