# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0012_upload_link'),
    ]

    operations = [
        migrations.RenameField(
            model_name='upload',
            old_name='link',
            new_name='uuid',
        ),
    ]
