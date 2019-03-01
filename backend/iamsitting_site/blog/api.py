from blog.api_views import PostViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('posts', PostViewset)
