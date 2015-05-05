from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from app import views

urlpatterns = patterns('',
    url(r'^home/$', views.home, name='home'),
    url(r'^$', views.index, name='index'),
    url(r'^base/$', views.base, name='index'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^aboutusurl/$', views.aboutusfun, name='aboutus'),
    url(r'^register/$', views.register, name='register'),
)
