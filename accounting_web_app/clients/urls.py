from django.conf.urls import patterns, url

from clients import views

urlpatterns = patterns('',
    url(r'^$', views.client, name='index')
)