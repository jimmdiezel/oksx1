# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oksx1a', '0026_auto_20170219_1657'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='results',
            new_name='assessment',
        ),
        migrations.RenameField(
            model_name='assessment',
            old_name='result_no',
            new_name='assessment_no',
        ),
        migrations.AlterField(
            model_name='executive',
            name='result',
            field=models.ForeignKey(related_name='exeResult', to='oksx1a.assessment', blank=True, null=True, to_field='assessment_no'),
        ),
        migrations.AlterField(
            model_name='location',
            name='result',
            field=models.ForeignKey(related_name='locResult', to='oksx1a.assessment', blank=True, null=True, to_field='assessment_no'),
        ),
        migrations.AlterField(
            model_name='test',
            name='result',
            field=models.ForeignKey(related_name='tesResult', to='oksx1a.assessment', blank=True, null=True, to_field='assessment_no'),
        ),
        migrations.AlterField(
            model_name='user',
            name='result',
            field=models.ForeignKey(related_name='useResult', to='oksx1a.assessment', blank=True, null=True, to_field='assessment_no'),
        ),
    ]
