from django.shortcuts import render, redirect

# Create your views here.

from django.http import HttpResponse

from . models import Task

from . forms import TaskForm

def home(request):

    form = TaskForm()

    tasks = Task.objects.all()

    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            form.save() 
        return redirect('/')
    context = {'tasks': tasks, 'TaskForm': form}

    return render(request,'home.html',context)


def update_task(request, pk):

    task = Task.objects.get(id=pk)

    form = TaskForm(instance=task )

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)

        if form.is_valid():

            form.save()

        return redirect('/')
    context = {'TaskForm': form}

    return render(request, 'update_task.html', context)

def delete_task(request, pk):

    task = Task.objects.get(id=pk)

    if request.method=='POST':
        task.delete()
        return redirect('')
    context = {'task':task}
    
    return render(request, 'delete_task.html', context)