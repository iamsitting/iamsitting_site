from django.urls import include, path, re_path
from django.views.generic import TemplateView
from demo.api import router
from demo import views

app_name = "demo"

urlpatterns = [
  path('api/', include(router.urls)),
  re_path(r'^get-patient-dose/(?P<pk>\d+)', views.get_calculations, name='patient-dose'),
  path('', TemplateView.as_view(template_name='demo/index.html'))
]
