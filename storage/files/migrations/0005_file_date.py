# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0004_auto_20150321_2053'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 21, 19, 29, 21, 941084, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
