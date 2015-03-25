# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0006_remove_file_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='name',
            field=models.FileField(upload_to='', default=0),
            preserve_default=False,
        ),
    ]
