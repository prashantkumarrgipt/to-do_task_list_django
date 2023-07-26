from django.shortcuts import get_object_or_404, redirect, render
from .models import Task
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from .forms import BulkTaskAddForm

def task_list(request):
    search_query = request.GET.get('search')
    if search_query:
        tasks = Task.objects.filter(title__icontains=search_query)
    else:
        tasks = Task.objects.all()
    return render(request, 'index.html', {'tasks': tasks})

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    print(task)
    task.delete()
    return redirect('task_list')

@csrf_protect
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == "POST":
        new_title = request.POST.get("title")
        task.title = new_title
        task.save()
    return redirect('task_list') 

@csrf_exempt
def complete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == "POST":
        data = json.loads(request.body)
        is_completed = data.get("is_completed")
        task.is_completed = bool(is_completed)
        task.save()
        return JsonResponse({"message": "Task completed successfully"})
    return redirect('task_list') 

def add_task(request):
    if request.method == "POST":
        title = request.POST.get("title")
        if title:
            task = Task.objects.create(title=title, is_completed=False)
            return redirect('task_list')  # Redirect to the task list page after adding the task
    return redirect('task_list')


def bulk_add_tasks(request):
    if request.method == 'POST':
        form = BulkTaskAddForm(request.POST)
        if form.is_valid():
            tasks_data = form.cleaned_data['tasks']
            task_titles = [title.strip() for title in tasks_data.split('\n') if title.strip()]
            for title in task_titles:
                Task.objects.create(title=title, is_completed=False)
            return redirect('task_list')  # Redirect to the task list page after adding tasks
    else:
        form = BulkTaskAddForm()

    return render(request, 'bulk_add_tasks.html', {'form': form})

def bulk_delete_tasks(request):
    if request.method == 'POST':
        task_ids = request.POST.getlist('task_ids')  # Get the list of selected task IDs
        tasks_to_delete = Task.objects.filter(id__in=task_ids)
        tasks_to_delete.delete()
    return redirect('task_list')