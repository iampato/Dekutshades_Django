# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-08-09 20:56
from __future__ import unicode_literals

from django.db import migrations
import django.utils.timezone
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_subscribe'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content',
            field=tinymce.models.HTMLField(default=django.utils.timezone.now, verbose_name='Content'),
            preserve_default=False,
        ),
    ]
