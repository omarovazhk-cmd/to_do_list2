from django.shortcuts import render
from webapp.models import Task

def task_list_view(request):
    tasks = Task.objects.all()
    context = {
        'tasks': tasks
    }
    return render(request, 'task_list.html', context)