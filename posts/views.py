# coding: utf-8
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.shortcuts import resolve_url
from models import *
from forms import *


# Create your views here.


class PostView(DetailView):

    queryset = Post.objects.all()
    template_name = "posts/one_post.html"


class BlogList(ListView):
    template_name = "posts/blog_list.html"
    model = Blog
    queryset = Blog.objects.all()
    sortform= None

    def dispatch(self, request, *args, **kwargs):
        self.sortform = SortFormBlogs(data= self.request.GET, initial={'sort': 'title'})
        return super(BlogList, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(BlogList, self).get_context_data(**kwargs)
        context['sortform'] = self.sortform
        return context

    def get_queryset(self):
        qs = super(BlogList, self).get_queryset()
        if self.sortform.is_valid():
            qs = qs.order_by(self.sortform.cleaned_data['sort'])
            if self.sortform.cleaned_data['search']:
                qs = qs.filter(title__icontains=self.sortform.cleaned_data['search'])
        return qs


class BlogView(DetailView):

    queryset = Blog.objects.all()
    template_name = "posts/blog.html"


class AddBlog(CreateView):

    template_name = 'posts/new_blog.html'
    model = Blog
    fields = ('title', 'description', 'categories')

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.rate = 0
        return super(AddBlog, self).form_valid(form)

    def get_success_url(self):
        return resolve_url('blogs:blog_list')


class EditBlog(UpdateView):
    template_name = 'posts/edit_blog.html'
    model = Blog
    fields = ('title', 'description', 'categories')

    def get_success_url(self):
        return resolve_url('blogs:one_blog', pk=self.object.pk)

    def get_queryset(self):
        return Blog.objects.filter(author=self.request.user)


class AddPost(CreateView):

    template_name = 'posts/new_post.html'
    model = Post
    fields = ('title', 'content', 'blog')

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.rate = 0
        return super(AddPost, self).form_valid(form)

    def get_form(self, form_class=None):
        form = super(AddPost,self).get_form()
        form.fields['blog'].queryset = Blog.objects.all().filter(author=self.request.user)
        return form

    def get_success_url(self):
        return resolve_url('blogs:one_blog', pk=self.object.blog.id)


class EditPost(UpdateView):
    template_name = 'posts/edit_post.html'
    model = Post
    fields = ('title', 'content')

    def get_success_url(self):
        return resolve_url('blogs:one_post', pk=self.object.pk, blog_id = self.object.blog.id)

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)