from django.conf.urls import url

from home_app import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^about_me/$', views.about_me, name='about_me'),
]
