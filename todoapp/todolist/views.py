from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from .models import ToDo
from .forms import TodoForm


# Create your views here.
def index(request):
    todos = ToDo.objects.all()
    return render(request, 'todoapp/index.html', {'todo_list': todos, 'title': 'Главная страница'})


@require_http_methods(['POST'])
@csrf_exempt
def add(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            todo = ToDo(title=title, description=description)
            todo.save()
            return redirect('index')
    else:
        form = TodoForm()
    return render(request, 'todoapp/index.html', {'form': form})


def update(request, todo_id):
    todo = ToDo.objects.get(id=todo_id)
    todo.completed = not todo.completed
    todo.save()
    return redirect('index')


def delete(request, todo_id):
    todo = ToDo.objects.get(id=todo_id)
    todo.delete()
    return redirect('index')


class Todo:
    pass


def edit_todo(request, todo_id):
    todo = ToDo.objects.get(id=todo_id)
    form = TodoForm(request.POST, instance=todo)

    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TodoForm(instance=todo)

    return render(request, 'todoapp/edit.html', {'form': form, 'todo': todo})

