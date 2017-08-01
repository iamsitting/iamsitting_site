from django.conf.urls import url

from blog import views

urlpatterns = [
    url(r'^newpost/$', views.NewPost.as_view(), name='newpost'),
    url(r'^editpost/(?P<slug>[-\w]+)$', views.EditPost.as_view(), name='editpost'),
    #url(r'^post/(?P<slug>[-\w]+)$', views.ShowPost(), name='post'),
]
