from django.shortcuts import render
from .models import Todo

def todo_list(request):
  todos = Todo.objects.all()
  return render(request, 'todoapp/list.html', {'todos': todos})
