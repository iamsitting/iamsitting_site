from django import forms

from blog.models import Post, Comment

class PostForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = ['title', 'subtitle', 'body', 'preview', 'category']

class CommentForm(forms.ModelForm):
  class Meta:
    model = Comment
    exclude = ['post']
