from django.shortcuts import render,HttpResponse,redirect
from .models import Task

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin # This 
from django.urls import reverse_lazy
from django.contrib.auth import logout  



# Create your views here.

# def Home(request):
#     return HttpResponse("hello")

# def Tasks(request):
#     tasks = Task.objects.all()
#     context  = {'tasks':tasks}
#     return render(request, 'base/tasks.html',context)

# class UserLogout(LogoutView):
#     template_name = 'base/AreYouSure.html'
#     success_url = 'tasksHome'

def UserLogout(request):  # creating this view to so that   
    logout(request)   # user presses the logout button then its session will be deleted from the database, and the user will be logged out
    return redirect('tasksHome')   # and the user is redirected to the home page..

class UserLogin(LoginView):
    template_name = 'base/UserLogin.html'
    fields = '__all__'
    redirect_authenticated_user = True # this allows us to redirect the user to the home page if they are already logged in. Meaning, if a user is alreadt login we will not show the login page to him again.
    # success_url = '/'
    success_url = '/'
    # def get_success_url(self):
    #     return reverse_lazy
    #############
    ####
    #
    
class TaskList(ListView,LoginRequiredMixin):
    model = Task
    template_name = 'base/tasksHome.html'
    context_object_name = 'tasks'   # This is used to specify the name of the object that we want to use in the template. In this case, we are using tasks as the object name

class TaskDetail(DetailView,LoginRequiredMixin):   # THis is used to go into the details of a each individual task
    model = Task
    template_name = 'base/task.html'
    context_object_name = 'task'

class TaskCreate(CreateView,LoginRequiredMixin):
    model = Task
    template_name = 'base/createTask.html'
    
    fields = 'title,description'.split(',')# this is used to specify the fields that we want to display in the form. if we want to display all the fields, we can use '__all__' instead of the list of fields. split is used to convert the string into a list of strings

    success_url = '/' # the purpose of this is to redirect to the home page after creating a new task
    # success_url = reverse_lazy('tasks') # another way to redirect to the home page after creating a new task. this is used when the url is not defined in the urls.py

class EditTask(UpdateView,LoginRequiredMixin):
    model = Task
    template_name = 'base/createTask.html'
    fields = "__all__"
    success_url = '/' # the purpose of this is to redirect to the home page after creating a new task

class DeleteTask(DeleteView,LoginRequiredMixin):
    model = Task
    template_name = 'base/delete.html'
    context_object_name = 'obj'
    success_url = '/' # the purpose of this is to redirect to the home page after creating a new task

#! Restricting Pages
#*  The mixin of LoginRequiredMixin will not allow the user to access the page if they are not logged in. It will redirect them to the login page.  We are redirected so we need to tell Django where should we be redirected after logging in. This is done by setting the LOGIN_URL in the settings.py file.