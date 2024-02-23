from django.shortcuts import render,HttpResponse
from .models import Task

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


# Create your views here.

# def Home(request):
#     return HttpResponse("hello")

# def Tasks(request):
#     tasks = Task.objects.all()
#     context  = {'tasks':tasks}
#     return render(request, 'base/tasks.html',context)


class TaskList(ListView):
    model = Task
    template_name = 'base/tasks.html'
    context_object_name = 'tasks'

class TaskDetail(DetailView):
    model = Task
    template_name = 'base/taskList.html'
    # context_object_name = 'task'
