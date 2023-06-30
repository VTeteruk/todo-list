from django.views import generic

from todo.models import Task


class IndexView(generic.TemplateView):
    template_name = "todo/index.html"


class TaskListView(generic.ListView):
    model = Task
    template_name = "todo/task_list.html"