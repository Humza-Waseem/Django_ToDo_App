from django.contrib import admin
from django.urls import path,include
# from . import views
from .views import TaskList,TaskDetail,TaskCreate,EditTask,DeleteTask,UserLogin,RegisterUser
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('',TaskList.as_view(),name = 'tasksHome'),
    path('UserLogin/',UserLogin.as_view(), name = "UserLogin"),
    path('Logout/',LogoutView.as_view(next_page = 'UserLogin'), name = 'UserLogout'),#we can set the next_page to the login page here as well as in the views.py file at the cbv of UserLogout
    path('RegisterUser/',RegisterUser, name = "RegisterUser"),

    # path('Logout/',UserLogout,name = 'UserLogout'),

    path('task/<str:pk>/',TaskDetail.as_view(), name = 'task'),
    path('create-task/',TaskCreate.as_view(), name = "create-task"),
    path('edit-task/<str:pk>/',EditTask.as_view(), name = "edit-task"),
    path('deleteTask/<str:pk>/',DeleteTask.as_view(), name = "delete-task"),

]
  #!##########   COMMENTS   ###############
 ##* as_view() is used to convert the class based views into function based views, which is required by the path function