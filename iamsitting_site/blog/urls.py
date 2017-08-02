from django.conf.urls import url

from blog import views

urlpatterns = [
    url(r'^new-post/$', views.NewPost.as_view(), name='new-post'),
    url(r'^edit-post/(?P<slug>[-\w]+)$', views.EditPost.as_view(), name='edit-post'),
    url(r'(?P<status>[ADP])/(?P<id>\d+)$', views.modify_post_status, name='modify-post-status'),
    url(r'^post-requests/$', views.PostRequests.as_view(), name='post-requests'),
    #url(r'^post/(?P<slug>[-\w]+)$', views.ShowPost(), name='post'),
]
