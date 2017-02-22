# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('oksx1a', '0023_event_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='address_no',
        ),
        migrations.AddField(
            model_name='address',
            name='result_no',
            field=models.UUIDField(editable=False, verbose_name='Address No', serialize=False, default=uuid.uuid4, primary_key=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='add1',
            field=models.CharField(default='Unknown', max_length=80, verbose_name='Address Line 1'),
        ),
        migrations.AlterField(
            model_name='results',
            name='result_no',
            field=models.UUIDField(editable=False, verbose_name='Result No', serialize=False, default=uuid.uuid4, primary_key=True),
        ),
    ]
