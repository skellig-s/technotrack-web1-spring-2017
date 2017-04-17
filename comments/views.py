from django.shortcuts import render, get_object_or_404, resolve_url, HttpResponse
from django.views.generic import DetailView, CreateView, View
from models import Comment
from posts.models import *
# Create your views here.

# class PostView(DetailView):
#
#     queryset = Comment.objects.all()
#     template_name = "comments/one_post.html"


class PostDetail(CreateView):

    model = Comment
    template_name = 'posts/one_post.html'
    fields = ('description', )
    postobject = None

    def dispatch(self, request, pk=None, *args, **kwargs):
        self.postobject = get_object_or_404(Post, id=pk)
        return super(PostDetail, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data(**kwargs)
        context['post'] = self.postobject
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.rate = 0
        form.instance.post = self.postobject
        return super(PostDetail, self).form_valid(form)

    def get_success_url(self):
        return resolve_url('blogs:one_post', pk=self.postobject.id, blog_id=self.postobject.blog_id)

# class CommentLikeCountView (View):
#
#     comment = None;
#
#     def dispatch(self, request, pk=None *args, **kwargs):
#         self.comment = get_object_or_404(Comment, pk = pk)
#         return super(CommentLikeCountView, self).dispatch(request, *args, **kwargs)
#
#     def get(self, request):
#         return HttpResponse(self.comment.like_set.count())