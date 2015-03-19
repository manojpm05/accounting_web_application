from models import clients
from models import projects
from django.shortcuts import render_to_response
from django.contrib import admin
admin.autodiscover()

 
def client(request): #Define our function
 
    items = clients.objects.all()
   
    return render_to_response('clients.html', {'items': items})
   
def project(request): #Define our function
    
    items = projects.objects.all()
    
    return render_to_response('projects.html', {'items': items})
    


