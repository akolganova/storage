# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload',
            name='uuid',
            field=models.CharField(unique=True, max_length=256, default=uuid.uuid1),
            preserve_default=True,
        ),
    ]
