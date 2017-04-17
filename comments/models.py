from __future__ import unicode_literals

from django.db import models
from django.conf import settings

# Create your models here.


class Comment(models.Model):
    post = models.ForeignKey('posts.Post')
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    description = models.TextField()
    rate = models.IntegerField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.description


class Like(models.Model):
    comment = models.ForeignKey('Comment')
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    created_at = models.DateField(auto_now_add=True)
