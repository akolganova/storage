# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import storage.files.models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0014_auto_20150322_1805'),
    ]

    operations = [
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('orig_file', models.FileField(storage=storage.files.models.MediaFileSystemStorage(), upload_to=storage.files.models.media_file_name)),
                ('md5sum', models.CharField(max_length=36)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='upload',
            name='md5sum',
        ),
        migrations.RemoveField(
            model_name='upload',
            name='orig_file',
        ),
    ]
