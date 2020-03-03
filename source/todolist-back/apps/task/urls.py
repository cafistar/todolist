from django.urls import path
from apps.task import views

app_name = 'task'

urlpatterns = [
    path('', views.TaskListView.as_view(), name='list'),
]
