# todos/urls.py
from django.urls import path
from .views import TodoListView

urlpatterns = [
    path('api/todos/', TodoListView.as_view(), name='todo_list'),
]
