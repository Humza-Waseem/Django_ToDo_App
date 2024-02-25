from django.shortcuts import render,HttpResponse
from .models import Task

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


# Create your views here.

# def Home(request):
#     return HttpResponse("hello")

# def Tasks(request):
#     tasks = Task.objects.all()
#     context  = {'tasks':tasks}
#     return render(request, 'base/tasks.html',context)


class TaskList(ListView):
    model = Task
    template_name = 'base/tasksHome.html'
    context_object_name = 'tasks'

class TaskDetail(DetailView): 
    model = Task
    template_name = 'base/task.html'
    context_object_name = 'task'

class TaskCreate(CreateView):
    model = Task
    template_name = 'base/createTask.html'
    
    fields = 'title,description'.split(',')# this is used to specify the fields that we want to display in the form. if we want to display all the fields, we can use '__all__' instead of the list of fields. split is used to convert the string into a list of strings

    success_url = '/' # the purpose of this is to redirect to the home page after creating a new task
    # success_url = reverse_lazy('tasks') # another way to redirect to the home page after creating a new task. this is used when the url is not defined in the urls.py

class EditTask(UpdateView):
    model = Task
    template_name = 'base/createTask.html'
    fields = "__all__"
    success_url = '/' # the purpose of this is to redirect to the home page after creating a new task

class DeleteTask(DeleteView):
    model = Task
    template_name = 'base/delete.html'
    context_object_name = 'obj'
    success_url = '/' # the purpose of this is to redirect to the home page after creating a new task