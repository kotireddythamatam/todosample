# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-16 14:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0004_auto_20181116_1339'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog_posts',
            name='tag',
        ),
    ]