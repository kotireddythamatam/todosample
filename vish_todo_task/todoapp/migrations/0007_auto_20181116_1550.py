# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-16 15:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0006_auto_20181116_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog_posts',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
