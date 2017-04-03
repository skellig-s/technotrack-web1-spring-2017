# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.conf.urls import url, include
from.views import *
from comments.views import PostDetail


urlpatterns = [
    url(r'^$', BlogList.as_view(), name="blog_list"),
    url(r'^(?P<pk>\d+)/$', BlogView.as_view(), name="one_blog"),
    url(r'^(?P<blog_id>\d+)/(?P<pk>\d+)/$', PostDetail.as_view(), name="one_post"),

    url(r'^new/$', login_required(AddBlog.as_view()), name='newBlog'),
    url(r'^(?P<pk>\d+)/edit/$', login_required(EditBlog.as_view()), name='editBlog'),
    url(r'^post/new/$', login_required(AddPost.as_view()), name='newPost'),
    url(r'^(?P<blog_id>\d+)/(?P<pk>\d+)/edit/$', EditPost.as_view(), name='editPost'),
]
