from models import clients
from models import projects

from django.http import HttpResponse

from django.shortcuts import render_to_response
from django.contrib import admin
admin.autodiscover()

def index(request): #Define our function
 
      
    return render_to_response('index.html')
   
 
def client(request): #Define our function
 
    items = clients.objects.all()
   
    return render_to_response('clients.html', {'items': items})
   
def project(request): #Define our function
    
    items = projects.objects.all()
    
    return render_to_response('projects.html', {'items': items})
    
def total(request): #Define our function
    
    items = projects.objects.all()
    
    return render_to_response('total.html', {'items': items})
    



