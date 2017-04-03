# coding: utf-8
from __future__ import unicode_literals

from django.db import models
# from application.settings import AUTH_USER_MODEL
from django.conf import settings

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'Категория'
        verbose_name_plural = u'Категории'
        ordering = ('name',)


class Blog(models.Model):

    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=255)
    description = models.TextField()
    rate = models.IntegerField()
    categories = models.ManyToManyField(Category, blank=True)

    def __unicode__(self):
        return self.title


class Post(models.Model):

    blog = models.ForeignKey(Blog)
    title = models.CharField(max_length=255)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    content = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title