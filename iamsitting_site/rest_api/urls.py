from django.conf.urls import url, include
from rest_framework import routers
from rest_api.viewsets import LocalImageViewSet
from rest_api import views

router = routers.DefaultRouter()
router.register('images', LocalImageViewSet, 'images')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
#    url(r'^images', views.UploadLocalImage.as_view(), name='images'),
]

