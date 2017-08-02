from django.contrib import admin
from blog.models import Post, Comment, Category

admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Comment)
