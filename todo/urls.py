from django.urls import path

from todo.views import (
    IndexView,
    TaskListView,
    TaskCreateView,
    TaskStatusUpdateView,
    TaskUpdateView,
    TaskDeleteView,
    TagListView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView,
)

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("tasks/", TaskListView.as_view(), name="tasks"),
    path("tasks/new/", TaskCreateView.as_view(), name="task-create"),
    path("task/<int:task_id>/status-update/", TaskStatusUpdateView.as_view(), name='task-status-update'),
    path("task/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("task/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path("tags", TagListView.as_view(), name="tags"),
    path("tags/new/", TagCreateView.as_view(), name="tag-create"),
    path("tag/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),
    path("tag/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete"),
]

app_name = "todo"
