# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0005_file_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='date',
        ),
    ]
