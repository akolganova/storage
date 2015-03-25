# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0003_fileattachment'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FileAttachment',
            new_name='Attachments',
        ),
    ]
