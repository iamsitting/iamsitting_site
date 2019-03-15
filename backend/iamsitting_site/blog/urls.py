from blog import views
from blog.api import router
from django.urls import include, path
from django.conf.urls import url
from django.views.generic import TemplateView

app_name = "blog"

urlpatterns = [
    path('api/', include(router.urls)),
    url(r'^view/(?P<slug>[-\w]+)$', views.view_post, name='post'),
    path('', TemplateView.as_view(template_name='blog/index.html'), name='home'),
    # url(r'(?P<status>[ADP])/(?P<id>\d+)$', views.modify_post_status, name='modify-post-status'),
    # url(r'^post-requests/$', views.PostRequests.as_view(), name='post-requests'),
]
