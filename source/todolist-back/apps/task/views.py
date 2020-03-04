from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
)

from apps.task.models import Task
from apps.task.serializers import TaskSerializer


class TaskListView(ListAPIView):
    queryset = Task.objects.active()
    serializer_class = TaskSerializer


class TaskCreateView(CreateAPIView):
    queryset = Task.objects.active()
    serializer_class = TaskSerializer
