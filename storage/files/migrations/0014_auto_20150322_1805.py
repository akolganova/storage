# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import storage.files.models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0013_auto_20150322_1608'),
    ]

    operations = [
        migrations.AddField(
            model_name='upload',
            name='md5sum',
            field=models.CharField(default=0, max_length=36),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='upload',
            name='orig_file',
            field=models.FileField(upload_to=storage.files.models.media_file_name, default=1),
            preserve_default=False,
        ),
    ]
