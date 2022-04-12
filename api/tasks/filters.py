from django_filters import FilterSet, MultipleChoiceFilter
from .models import Task, Project, TaskSession

class TaskFilter(FilterSet):
    class Meta:
        model = Task
        fields = {
            'id': ['exact'],
            'name': ['icontains','istartswith'],
            'status': ['exact'],
            'project__id': ['exact'],
        }