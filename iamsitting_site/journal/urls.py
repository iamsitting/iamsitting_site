from django.urls import include, path
from django.views.generic import TemplateView

from .api import router

app_name = "journal"

urlpatterns = [
  path('api/', include(router.urls)),
  path('', TemplateView.as_view(template_name='index.html')),
]
