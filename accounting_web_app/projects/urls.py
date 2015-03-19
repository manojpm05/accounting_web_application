from django.conf.urls import patterns, url

from clients import views

urlpatterns = patterns('',
    url(r'^$', views.project, name='index')
)