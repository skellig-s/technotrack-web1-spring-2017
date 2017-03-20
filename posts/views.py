from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from models import *
from comments.models import Comment
from django.views.generic.base import TemplateView


# Create your views here.


# def showPost(request, blog_id=None, post_id=None):
#     # post = Post.objects.get(id=post_id, blog_id=blog_id)
#     post = get_object_or_404(Post, pk=post_id, blog_id=post_id)
#     return render(request, 'posts/one_post.html',
#                   {"post": post})


class PostView(DetailView):

    queryset = Post.objects.all()
    template_name = "posts/one_post.html"


class BlogList(ListView):
    template_name = "posts/blog_list.html"
    model = Blog


class BlogView(DetailView):

    queryset = Blog.objects.all()
    template_name = "posts/blog.html"


class HomePageView(TemplateView):

    template_name = "posts/home.html"
    title = "Main page"
    totallyBlogs = Blog.objects.all().count()
    totallyPosts = Post.objects.all().count()
    totallyComments = Comment.objects.all().count()

    # def blogs(self):
    #     return Blog.objects.all()
    #  create view variable
    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['latest_blogs'] = Blog.objects.all()[:5]
        return context
