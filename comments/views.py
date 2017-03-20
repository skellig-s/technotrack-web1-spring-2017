from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from models import Comment
from posts.models import *
# Create your views here.

# class PostView(DetailView):
#
#     queryset = Comment.objects.all()
#     template_name = "comments/one_post.html"
