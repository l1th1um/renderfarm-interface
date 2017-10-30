# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-30 13:33
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='project_uuid',
            field=models.UUIDField(default=uuid.uuid4),
        ),
        migrations.AddField(
            model_name='project',
            name='status',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_file',
            field=models.FileField(upload_to='static/uploads/project_file/', validators=[django.core.validators.FileExtensionValidator(['zip'])]),
        ),
    ]
