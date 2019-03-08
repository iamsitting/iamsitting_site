from blog import views
from blog.api import router
from django.urls import include, path
from django.views.generic import TemplateView

app_name = "blog"

urlpatterns = [
    path('api/', include(router.urls)),
    path('', TemplateView.as_view(template_name='blog/index.html')),
    # url(r'^new-post/$', views.NewPost.as_view(), name='new-post'),
    # url(r'^edit-post/(?P<slug>[-\w]+)$', views.EditPost.as_view(), name='edit-post'),
    # url(r'(?P<status>[ADP])/(?P<id>\d+)$', views.modify_post_status, name='modify-post-status'),
    # url(r'^post-requests/$', views.PostRequests.as_view(), name='post-requests'),
    # url(r'^view/(?P<slug>[-\w]+)$', views.view_post, name='post'),
    # url(r'^upload-image', views.upload_image, name='upload-image'),
]
