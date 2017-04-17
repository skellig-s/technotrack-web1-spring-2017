from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.base import TemplateView
from comments.models import Comment
from posts.models import *
from forms import RegistrationForm
from django.views.generic import FormView
from django.shortcuts import resolve_url

from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect


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
        delta = 5
        if totallyBlogs < 5:
            delta = totallyBlogs
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['latest_blogs'] = Blog.objects.all()[totallyBlogs-delta:totallyBlogs]
        return context


class RegistrationFormView(FormView):
    form_class = RegistrationForm
    template_name = 'core/registration.html'

    def form_valid(self, form):
        form.save()
        return super(RegistrationFormView, self).form_valid(form)

    def get_success_url(self):
        return resolve_url('login')


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('home')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'core/change_password.html', {
        'form': form
    })