from django.shortcuts import render

from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView, FormView, UpdateView
from django.views.generic import TemplateView
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from blog.forms import PostForm, CommentForm
from blog.models import Post, Comment, Category

class NewPost(CreateView):
    model = Post
    template_name = 'blog/newpost.html'
    form_class = PostForm

    def get_context_data(self, **kwargs):
      ctx = super(NewPost, self).get_context_data(**kwargs)
      return ctx
