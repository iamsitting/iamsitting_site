from django import forms

from blog.models import Comment, Post


class PostForm(forms.ModelForm):
  preview = forms.CharField(required=False)

  class Meta:
    model = Post
    fields = ['title', 'subtitle', 'body', 'category']


class CommentForm(forms.ModelForm):
  class Meta:
    model = Comment
    exclude = ['post']


class LocalImageForm(forms.ModelForm):
  file = forms.ImageField()
