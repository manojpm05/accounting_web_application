from django.db import models
from django.db.models import Sum

class clients(models.Model):
    Name = models.CharField(max_length=200)
    Email = models.CharField(max_length=200)
    Company_info = models.CharField(max_length=200)
    
class projects(models.Model):
    clients = models.ForeignKey(clients)
    Name_of_the_project = models.CharField(max_length=200)
    Technology_used = models.CharField(max_length=200)
    Start_date = models.DateTimeField('Start date')
    Hours_spent = models.PositiveIntegerField(primary_key=True)
    Per_hour_cost = models.PositiveIntegerField(primary_key=True)
    
class total(models.Model):
    Hours_spent = models.ForeignKey(projects)
    