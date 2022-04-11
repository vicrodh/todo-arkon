from pyexpat import model
from django.db import models
from core.user.models import User

# Create your models here.

class Project(models.Model):
    name = models.CharField

class Task(models.Model):

    STATUS_CHOICES = [
        ('pending','Pending'),
        ('wip','Work in progress'),
        ('completed','Completed'),
        ('deleted','Deleted'),
    ]    
    name = models.CharField(max_length=256, blank=False, null=True)
    project = models.ForeignKey(Project)                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
    create_date = models.DateField()
    estimated_length = models.DurationField()
    final_lenght = models.DurationField()
    status = models.CharField(max_length=32, choices=STATUS_CHOICES, default='pending')
    created_by = models.ForeignKey(User)
    owned_by = models.ForeignKey(User)

    pass

class TaskSession(models.Model):
    pass