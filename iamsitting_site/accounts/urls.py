from django.conf.urls import include, url

from accounts import views

app_name = "accounts"

urlpatterns = [
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^signup/$', views.signup, name='signup'),
]
