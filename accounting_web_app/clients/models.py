from django.db import models

class clients(models.Model):
    Name = models.CharField(max_length=200)
    Email = models.CharField(max_length=200)
    Company_info = models.CharField(max_length=200)
    
class projects(models.Model):
    clients = models.ForeignKey(clients)
    Name_of_the_project = models.CharField(max_length=200)
    Technology_used = models.CharField(max_length=200)
    Start_date = models.DateTimeField('date published')
    Hours_spent = models.PositiveIntegerField()
    Per_hour_cost = models.PositiveIntegerField()
   
