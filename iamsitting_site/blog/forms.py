from django import forms

from blog.models import Post, Comment

class PostForm(forms.ModelForm):
  preview = forms.CharField(required=False)
  class Meta:
    model = Post
    fields = ['title', 'subtitle', 'body', 'category']

class CommentForm(forms.ModelForm):
  class Meta:
    model = Comment
    exclude = ['post']
