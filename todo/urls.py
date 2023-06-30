from django.urls import path

from todo.views import IndexView, TaskListView, TaskCreateView

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("tasks/", TaskListView.as_view(), name="tasks"),
    path("tasks/new/", TaskCreateView.as_view(), name="task-create"),
]

app_name = "todo"
