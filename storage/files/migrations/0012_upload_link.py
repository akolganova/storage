# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0011_auto_20150322_0025'),
    ]

    operations = [
        migrations.AddField(
            model_name='upload',
            name='link',
            field=models.CharField(max_length=256, default=0),
            preserve_default=False,
        ),
    ]
