from email.policy import default
from django.db import models
from core.user.models import User

"""
Simple Project class model to help encapsulate
tasks grouping it by projects.
"""
class Project(models.Model):
    name = models.CharField
    created_by = models.ForeignKey(User, on_delete=models.RESTRICT,related_name="pr_created_by",)

"""
Task class model, required fields by business test case brief. 
Additional fields.
created_by - User FK. Thinking about expandable functions where, may bea manager could create 
task or bypass tasks to someone else
assigned_to - User FK. User working on the task
"""

class Task(models.Model):

    STATUS_CHOICES = [
        ('pending','Pending'),
        ('wip','Work in progress'),
        ('completed','Completed'),
        ('deleted','Deleted'),
    ]    
    name = models.CharField(max_length=256, blank=False, null=True)
    project = models.ForeignKey(Project, on_delete=models.RESTRICT,)                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    modified_at = models.DateTimeField(auto_now=True, null=True)
    estimated_length = models.DurationField()
    final_lenght = models.DurationField()
    status = models.CharField(max_length=32, choices=STATUS_CHOICES, default='pending')
    created_by = models.ForeignKey(User, on_delete=models.RESTRICT,related_name="tsk_created_by", null=True, blank=True)
    assigned_to = models.ForeignKey(User, on_delete=models.RESTRICT,related_name="tsk_assigned_to", null=True, blank=True)

"""
Task session class model. Instead of using a single updatable field
this class means to track the work on each class. First to get a more
accurate aproach of how the advance on the task was done, also letting 
open the option to track multiple users working on a single task. 

"""
class TaskSession(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="task_session", null=True, blank=True)
    init_date = models.DateTimeField(auto_now=True, null=True)
    final_lenght = models.DurationField(blank=False, null=True)
    user = models.ForeignKey(User, on_delete=models.RESTRICT,related_name="session_user", null=True, blank=True)
