# -*- coding: utf-8 -*-

from django.conf.urls import url
from core.views import HomePageView, RegistrationFormView
from django.contrib.auth.views import login, logout


urlpatterns = [
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^login/$', login, {'template_name': 'core/login.html'}, name='login'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^registr/$', RegistrationFormView.as_view(), name='registr'),
]
