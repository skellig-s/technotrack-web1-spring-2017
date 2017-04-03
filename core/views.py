from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from django.views.generic.base import TemplateView
from comments.models import Comment
from posts.models import *
from forms import RegistrationForm
from django.views.generic import FormView
from django.shortcuts import resolve_url


class HomePageView(TemplateView):

    template_name = "core/home.html"
    title = "Main page"
    totallyBlogs = Blog.objects.all().count()
    totallyPosts = Post.objects.all().count()
    totallyComments = Comment.objects.all().count()

    # def blogs(self):
    #     return Blog.objects.all()
    #  create view variable
    def get_context_data(self, **kwargs):
        totallyBlogs = Blog.objects.all().count()
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['latest_blogs'] = Blog.objects.all()[totallyBlogs-5:totallyBlogs]
        return context


class RegistrationFormView(FormView):
    form_class = RegistrationForm
    template_name = 'core/registration.html'

    def form_valid(self, form):
        form.save()
        return super(RegistrationFormView, self).form_valid(form)

    def get_success_url(self):
        return resolve_url('login')