# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-08-09 18:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('welcome', '0007_auto_20180809_2110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='published', max_length=10),
        ),
    ]