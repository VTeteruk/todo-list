from django.urls import path

from todo.views import IndexView, TaskListView

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("tasks/", TaskListView.as_view(), name="tasks")
]

app_name = "todo"
