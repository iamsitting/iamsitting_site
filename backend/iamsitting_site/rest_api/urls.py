from django.conf.urls import include, url
from rest_framework import routers

from rest_api import views
from rest_api.viewsets import LocalImageViewSet

app_name = "rest_api"

router = routers.DefaultRouter()
router.register('images', LocalImageViewSet, 'images')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
#    url(r'^images', views.UploadLocalImage.as_view(), name='images'),
]
