# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import storage.files.models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0015_auto_20150322_1854'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Media',
        ),
        migrations.AddField(
            model_name='upload',
            name='md5sum',
            field=models.CharField(max_length=36, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='upload',
            name='orig_file',
            field=models.FileField(upload_to=storage.files.models.media_file_name, storage=storage.files.models.MediaFileSystemStorage(), default=1),
            preserve_default=False,
        ),
    ]
