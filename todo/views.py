from django.http import HttpResponse, HttpRequest
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic

from todo.models import Task, Tag


class IndexView(generic.TemplateView):
    template_name = "todo/index.html"


class TaskListView(generic.ListView):
    model = Task
    template_name = "todo/task_list.html"


class TaskCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
    template_name = "todo/task_form.html"
    success_url = reverse_lazy("todo:tasks")


class TaskStatusUpdateView(generic.View):
    @staticmethod
    def get(request: HttpRequest, task_id: int) -> HttpResponse:
        task = Task.objects.get(pk=task_id)
        task.toggle_status()
        return redirect("todo:tasks")


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = "__all__"
    template_name = "todo/task_form.html"
    success_url = reverse_lazy("todo:tasks")


class TaskDeleteView(generic.DeleteView):
    model = Task
    template_name = "todo/task_delete.html"
    success_url = reverse_lazy("todo:tasks")


class TagListView(generic.ListView):
    model = Tag
    template_name = "todo/tag_list.html"


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo:tags")
    template_name = "todo/tag_form.html"


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    template_name = "todo/tag_form.html"
    success_url = reverse_lazy("todo:tags")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("todo:tags")
    template_name = "todo/tag_delete.html"
