from django.conf.urls import patterns, url,include
from django.contrib import admin
from clients import views


urlpatterns = patterns('',
    url(r'^clients/', include('clients.urls')), 
    url(r'^projects/', include('projects.urls')),    
    url(r'^total/', include('total.urls')),      
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
)
