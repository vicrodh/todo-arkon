from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, mixins, viewsets
from .filters import TaskFilter
from .models import Project, Task, TaskSession
from .serializers import (ProjectSerializer, TaskSerializer,
                          TaskSessionSerializer)

# Create your views here.

class TaskSet(viewsets.ModelViewSet):
    queryset = Task.objects.all();
    serializer_class = TaskSerializer
    filter_backends = (filters.OrderingFilter, DjangoFilterBackend)
    filter_class = TaskFilter
