# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-06 08:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='nothing',
            field=models.CharField(default='nothing hi', max_length=10),
            preserve_default=False,
        ),
    ]
