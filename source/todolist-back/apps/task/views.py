from rest_framework.generics import ListAPIView

from apps.task.models import Task
from apps.task.serializers import TaskSerializer


class TaskListView(ListAPIView):
    queryset = Task.objects.active()
    serializer_class = TaskSerializer
