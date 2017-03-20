# -*- coding: utf-8 -*-

from django.conf.urls import url, include
from.views import *
from comments.views import PostView

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', PostView.as_view(), name="one_post"),
]