from django.urls import path

from todo.views import IndexView

urlpatterns = [
    path("", IndexView.as_view(), name="index")
]

app_name = "todo"
