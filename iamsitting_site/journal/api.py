from rest_framework import routers

from .api_views import ArticleViewset, CategoryViewset, CommentViewset

router = routers.DefaultRouter()
router.register(r'articles', ArticleViewset)
router.register(r'comments', CommentViewset)
router.register(r'categories', CategoryViewset)
