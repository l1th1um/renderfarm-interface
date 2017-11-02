# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-02 14:20
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_auto_20171102_2041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_file',
            field=models.FileField(upload_to='static/uploads/project_file/', validators=[django.core.validators.FileExtensionValidator(['zip'])]),
        ),
    ]
