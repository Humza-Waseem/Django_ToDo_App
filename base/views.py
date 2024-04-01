from django.shortcuts import render,HttpResponse,redirect
from .models import Task

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth import login # this is used to login the user after they have registered
from django.contrib.auth.forms import UserCreationForm # this allows us to create a form for the user to register, we can customize this form as well
from django.views.generic import FormView



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

# def UserLogout(request):  # creating this view to so that   
#     logout(request)   # user presses the logout button then its session will be deleted from the database, and the user will be logged out
#     return redirect('tasksHome')   # and the user is redirected to the home page..


class UserLogin(LoginView):
    template_name = 'base/UserLogin.html'
    fields = '__all__'
    
    
    redirect_authenticated_user = True # this allows us to redirect the user to the home page if they are already logged in. Meaning, if a user is already login we will not show the login page to him again even if the user enters the address in the search bar.
    
    def get_success_url(self):
        return reverse_lazy('tasksHome')


#this is a Function Based View for registering the user
def RegisterUser(request):  
    page = 'register' 
   
    form = UserCreationForm()
    if request.method == 'POST':
        
        # form = UserCreationForm(request.POST)   # using MyUserCreationForm because it has our custom user model form
        if form.is_valid():
            user = form.save(commit=False)#commit = False means that we are not saving the form yet
            user.username = user.username
            user.save()
            login(request,user)
            return redirect('tasksHome')
        else:
            messages.error(request,'An error occured during registration')
    context = {'form':form,'page':page}
    return render(request,'base/UserLogin.html',context)


class RegisterUser(FormView):    

    template_name = 'base/UserLogin.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('tasksHome')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.save()
        if user is not None:
            login(self.request,user)
        return super(RegisterUser, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = self.request.GET.get('page', 'register')  # Default to register
        return context
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasksHome')
        return super(RegisterUser, self).get(*args, **kwargs)

    
    
class TaskList(LoginRequiredMixin,ListView):  
    model = Task
    template_name = 'base/tasksHome.html'
    context_object_name = 'tasks'   # This is used to specify the name of the object that we want to use in the template. In this case, we are using tasks as the object name
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user) # this allows us to filter the tasks based on the user that is logged in. This will only show the tasks that are created by the user that is logged in
        context['count'] = context['tasks'].filter(complete = False).count() # this will count the number of tasks that are not completed
        search_input = self.request.GET.get('TextIamSearching') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(title__icontains = search_input)
        context['search_input'] = search_input

       
        return context
        




class TaskDetail(LoginRequiredMixin,DetailView):   # THis is used to go into the details of a each individual task
    model = Task
    template_name = 'base/task.html'
    context_object_name = 'task'

class TaskCreate(LoginRequiredMixin,CreateView):
    model = Task
    template_name = 'base/createTask.html'
    
    fields = 'title,description,complete'.split(',')# this is used to specify the fields that we want to display in the form. if we want to display all the fields, we can use '__all__' instead of the list of fields. split is used to convert the string into a list of strings

    success_url = '/' # the purpose of this is to redirect to the home page after creating a new task
    # success_url = reverse_lazy('tasks') # another way to redirect to the home page after creating a new task. this is used when the url is not defined in the urls.py
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)

class EditTask(LoginRequiredMixin,UpdateView):
    model = Task
    template_name = 'base/createTask.html'
    fields = 'title,description,complete'.split(',')
    success_url = '/' # the purpose of this is to redirect to the home page after creating a new task

class DeleteTask(LoginRequiredMixin,DeleteView):
    model = Task
    template_name = 'base/delete.html'
    context_object_name = 'obj'
    success_url = '/' # the purpose of this is to redirect to the home page after creating a new task

#! Restricting Pages
#*  The mixin of LoginRequiredMixin will not allow the user to access the page if they are not logged in. It will redirect them to the login page.  We are redirected so we need to tell Django where should we be redirected after logging in. This is done by setting the LOGIN_URL in the settings.py file.








from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

class AuthMixin(LoginRequiredMixin):
    login_url = '/login/'  # Redirect URL for unauthenticated users

class HomePageView(AuthMixin, TemplateView):
    template_name = 'home.html'
