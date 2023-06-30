from django.http import HttpResponse, HttpRequest
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic

from todo.models import Task


class IndexView(generic.TemplateView):
    template_name = "todo/index.html"


class TaskListView(generic.ListView):
    model = Task
    template_name = "todo/task_list.html"


class TaskCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
    template_name = "todo/task_create.html"
    success_url = reverse_lazy("todo:tasks")


class TaskStatusUpdateView(generic.View):
    @staticmethod
    def get(request: HttpRequest, task_id: int) -> HttpResponse:
        task = Task.objects.get(pk=task_id)
        task.toggle_status()
        return redirect("todo:tasks")
