from blog.models import Post
from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('username', 'id')


class PostSerializer(serializers.ModelSerializer):

  author = UserSerializer(read_only=True)

  class Meta:
    model = Post
    fields = ('author', 'title', 'subtitle', 'body', 'category', 'id')
