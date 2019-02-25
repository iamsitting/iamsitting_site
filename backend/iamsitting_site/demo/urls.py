from django.urls import include, path
from django.views.generic import TemplateView
from demo.api import router

app_name = "demo"

urlpatterns = [
  path('api/', include(router.urls)),
  path('', TemplateView.as_view(template_name='demo/index.html'))
]
