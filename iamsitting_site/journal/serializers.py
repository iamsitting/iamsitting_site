from rest_framework import serializers

from .models import Article, Category, Comment


class ArticleSerializer(serializers.ModelSerializer):
  class Meta:
    model = Article
    fields = ('author', 'title', 'body', 'subtitle', 'category')


class CategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = Category
    fields = ('title')


class CommentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Comment
    fields = ('name', 'text', 'created_on')
