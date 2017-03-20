# -*- coding: utf-8 -*-

from django.conf.urls import url, include
from.views import *

urlpatterns = [
    url(r'^$', BlogList.as_view(), name="blog_list"),
    url(r'^(?P<pk>\d+)/$', BlogView.as_view(), name="one_blog"),
    # url(r'^(?P<blog_id>\d+)/post/', include('comments.urls', namespace="comments")),
    url(r'^(?P<blog_id>\d+)/(?P<pk>\d+)/$', PostView.as_view(), name="one_post"),
]
