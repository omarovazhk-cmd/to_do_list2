from django.shortcuts import render, redirect, get_object_or_404
from webapp.models import Task


def task_list_view(request):
    tasks = Task.objects.all()
    context = {
        'tasks': tasks
    }
    return render(request, 'task_list.html', context)


def task_create_view(request):
    if request.method == 'POST':
        description = request.POST.get('description')
        status = request.POST.get('status')
        due_date = request.POST.get('due_date')

        if description:
            Task.objects.create(
                description=description,
                status=status,
                due_date=due_date
            )
        return redirect('task_list')

    return render(request, 'task_create.html')


def task_delete_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
    return redirect('task_list')
