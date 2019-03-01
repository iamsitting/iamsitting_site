from blog.models import Post
from blog.serializers import PostSerializer
from rest_framework import filters, viewsets


class PostViewset(viewsets.ModelViewSet):
  queryset = Post.objects.all()
  serializer_class = PostSerializer
  filter_backends = (filters.SearchFilter, )
  search_fields = ('author__username', 'title', 'subtitle', )
