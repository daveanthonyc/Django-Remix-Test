# todos/views.py
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import JsonResponse
from django.views import View  # Import View class
from .models import Todo

@method_decorator(csrf_exempt, name='dispatch')
class TodoListView(View):
    def get(self, request):
        todos = Todo.objects.all()
        todos_data = [{"title": todo.title, "description": todo.description, "completed": todo.completed} for todo in todos]
        return JsonResponse(todos_data, safe=False)

    def post(self, request):
        todo = Todo(title="My first todo", description="This has worked successfully so cooool", completed=False)
        todo.save()

        todo_data = {
            "title": todo.id, 
            "description": todo.description, 
            "completed": todo.completed
        }

        return JsonResponse(todo_data)
