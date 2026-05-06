from django.shortcuts import render, redirect, get_object_or_404
from . import serializers
from Tasks.models import Task
from rest_framework import generics

from .serializers import TaskSerializer


class TaskAPIList(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskAPIDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


def Home(request):
    if request.method == 'POST':
        if "add_task" in request.POST:
            name = request.POST.get('title')
            priority = request.POST.get('priority')
            text = request.POST.get('text')
            if name and priority:
                Task.objects.create(title=name, priority=priority, description=text)

        if "complete_task" in request.POST:
            task_id = request.POST.get('task_id')
            task = Task.objects.get(id=task_id)
            task.completed = True
            task.save()

        return redirect("/")

    tasks = Task.objects.filter(completed=False).order_by('-priority')
    context = {'tasks': tasks}
    return render(request, 'Tasks/home.html', context)

def Completed(request):
    tasks = Task.objects.filter(completed=True)
    context = {'tasks': tasks}
    return render(request, 'Tasks/completed_task.html', context)

def Urgent(request):
    tasks = Task.objects.filter(priority__gte=4).order_by('-priority')
    context = {'tasks': tasks}
    return render(request, 'Tasks/urgent.html', context)

def delete(request, pk):
    task = get_object_or_404(Task, id=pk)
    task.delete()
    return redirect(request.META.get('HTTP_REFERER', '/'))





