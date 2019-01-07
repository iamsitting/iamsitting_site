from django.conf.urls import url

from home_app import views

app_name = "home_app"

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^about-me/$', views.about_me, name='about_me'),
    url(r'^contact-me/$', views.contact_me, name='contact-me'),
    url(r'^cv/$', views.my_cv, name='my_cv'),
    url(r'^cycle-x-pro', views.cycle_x_pro, name='cycle_x_pro'),
]
