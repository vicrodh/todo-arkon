# api/tasks/serializers.py

from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import Project, Task, TaskSession


class TaskSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskSession
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    task_sessions = TaskSessionSerializer(many=True)
    class Meta:
        model = Task
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Project
        fields = '__all__'

