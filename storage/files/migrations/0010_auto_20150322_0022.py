# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0009_auto_20150321_2305'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploads',
            name='mime_type',
            field=models.CharField(blank=True, max_length=256),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='uploads',
            name='name',
            field=models.CharField(max_length=256),
            preserve_default=True,
        ),
    ]
