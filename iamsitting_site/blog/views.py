import logging

from blog.forms import LocalImageForm, PostForm
from blog.models import Post
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView

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
    new_post.author = User.objects.get(id=self.request.user.id)
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
    pending_posts = Post.objects.exclude(id=post.id).filter(Q(author=self.request.user) & Q(status='P'))
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


class PostRequests(TemplateView):
  model = Post
  template_name = 'blog/post_requests.html'

  def get_context_data(self, **kwargs):
    ctx = super(PostRequests, self).get_context_data(**kwargs)
    pending_posts = Post.objects.filter(status='P')
    ctx['pending_posts'] = pending_posts
    return ctx


@user_passes_test(lambda u: u.is_superuser)
def modify_post_status(request, status, id):
  post = get_object_or_404(Post, pk=id)
  post.status = status
  post.save()
  return redirect(reverse('blog:post-requests'))


@csrf_exempt
def upload_image(request):
  if request.method == 'POST':
    form = LocalImageForm(request.POST, request.FILES)
    if form.is_valid():
      img = form.save(commit=False)
      img.save()
      return HttpResponse('image upload success')


def view_post(request, slug):
  print(slug)
  post = Post.objects.get(slug=slug)
  ctx = {'post': post}
  return render(request, 'blog/view_post.html', context=ctx)
