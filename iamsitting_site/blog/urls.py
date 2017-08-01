from django.conf.urls import url

from blog import views

urlpatterns = [
    url(r'^newpost/$', views.NewPost.as_view(), name='newpost'),
    #url(r'^$', views.home, name='home'),
    #url(r'^aboutme/$', views.aboutme, name='aboutme'),
]
