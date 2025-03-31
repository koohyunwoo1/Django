from django.shortcuts import render, redirect
from .models import Todo

# 할 일을 보여주는 함수
def todo_list(request):
    todos = Todo.objects.all() #  Todo 모델에서 모든 할 일을 가져온다.
    return render(request, 'myapp/todo_list.html', {'todos': todos}) # 템플릿을 렌더링하고 todos 데이터를 전달한다.

# 할 일을 추가하는 함수
def add_todo(request):
    if request.method == 'POST':
        print(request.POST)
        task = request.POST.get('task')
        Todo.objects.create(task=task)
        return redirect('todo_list')
    return render(request, 'myapp/add_todo.html')
