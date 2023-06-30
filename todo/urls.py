from django.urls import path

from todo.views import IndexView, TaskListView, TaskCreateView, TaskStatusUpdateView

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("tasks/", TaskListView.as_view(), name="tasks"),
    path("tasks/new/", TaskCreateView.as_view(), name="task-create"),
    path("task/<int:task_id>/status-update/", TaskStatusUpdateView.as_view(), name='task-status-update'),
]

app_name = "todo"
