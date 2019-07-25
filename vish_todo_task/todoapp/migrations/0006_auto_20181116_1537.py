# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-16 15:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0005_remove_blog_posts_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog_posts',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blog_posts',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]