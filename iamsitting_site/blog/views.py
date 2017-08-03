from django.shortcuts import render
from django.contrib.auth.models import User

from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView, FormView, UpdateView
from django.views.generic import TemplateView
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.db.models import Q

from blog.forms import PostForm, CommentForm
from blog.models import Post, Comment, Category

import logging

debug = logging.getLogger('debugger')
class NewPost(CreateView):
  model = Post
  template_name = 'blog/postform.html'
  form_class = PostForm

  def get_context_data(self, **kwargs):
    ctx = super(NewPost, self).get_context_data(**kwargs)
    posts = Post.objects.all().filter(author=self.request.user).order_by("-posted_on")
    ctx['posts'] = posts
    ctx['page_title'] = 'New Post'
    ctx['button_value'] = 'Submit'
    return ctx

  def form_valid(self, form):
    new_post = form.save(commit=False)
    new_post.author = User.objects.get(id = self.request.user.id)
    if self.request.user.is_superuser:
      new_post.status = 'A'
    new_post.save()
    return HttpResponseRedirect(reverse('blog:new-post'))

class EditPost(UpdateView):
  model = Post
  template_name = 'blog/postform.html'
  form_class = PostForm
  context_object_name = 'post'

  def get_context_data(self, **kwargs):
    ctx = super(EditPost, self).get_context_data(**kwargs)
    post = self.get_object()
    pending_posts = Post.objects.exclude(id=post.id).filter(Q(author=self.request.user)&Q(status='P'))
    ctx['posts'] = pending_posts
    ctx['page_title'] = 'Edit Post'
    ctx['button_value'] = 'Edit'
    return ctx

  def form_valid(self, form):
    post = form.save(commit=False)
    if post.status == 'D':
      post.status = 'P'
    post.save()
    return HttpResponseRedirect(reverse('blog:new-post'))
# TODO: set permissions
class PostRequests(TemplateView):
  model = Post
  template_name = 'blog/post_requests.html'

  def get_context_data(self, **kwargs):
    ctx = super(PostRequests, self).get_context_data(**kwargs)
    pending_posts = Post.objects.filter(status='P')
    ctx['pending_posts'] = pending_posts
    return ctx

def modify_post_status(request, status, id):
  post = get_object_or_404(Post, pk=id)
  post.status = status
  post.save()
  return redirect(reverse('blog:post-requests'))
#TODO: set permissions
def view_post(request, slug):
  post = Post.objects.get(slug=slug)
  ctx = {'post':post}
  return render(request, 'blog/view_post.html', context=ctx)
