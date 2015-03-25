# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('files', '0010_auto_20150322_0022'),
    ]

    operations = [
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('file', models.FileField(upload_to='%Y/%m/%d')),
                ('name', models.CharField(max_length=256)),
                ('content_type', models.CharField(blank=True, max_length=256)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RenameModel(
            old_name='Attachments',
            new_name='Attachment',
        ),
        migrations.RemoveField(
            model_name='uploads',
            name='user',
        ),
        migrations.DeleteModel(
            name='Uploads',
        ),
    ]
