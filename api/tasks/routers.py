from rest_framework.routers import DefaultRouter
from tasks.views import TaskSet

routes = DefaultRouter()

routes.register(r'task', TaskSet, basename='task')

urlpatterns = [
    *routes.urls
]
