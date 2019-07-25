# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

STATUS_CHOICES = (
    ('pending','PENDING'),
    ('in progress','IN PROGRESS'),
    ('completed','COMPLETED'),

)


class blog_posts(models.Model):
    title = models.CharField(max_length=400)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='pending')

    def __unicode__(self):
        return self.title

    def get_post_url(self):
        return reverse('post_edit', kwargs={'pk': self.pk})
