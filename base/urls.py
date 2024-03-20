from django.contrib import admin
from django.urls import path,include
# from . import views
from .views import TaskList,TaskDetail,TaskCreate,EditTask,DeleteTask,UserLogin
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('',TaskList.as_view(),name = 'tasksHome'),
    path('UserLogin/',UserLogin.as_view(), name = "UserLogin"),
    path('UserLogout/',LogoutView.as_view(next_page= 'UserLogin'), name = 'UserLogout'),
    path('task/<str:pk>/',TaskDetail.as_view(), name = 'task'),
    path('create-task/',TaskCreate.as_view(), name = "create-task"),
    path('edit-task/<str:pk>/',EditTask.as_view(), name = "edit-task"),
    path('deleteTask/<str:pk>/',DeleteTask.as_view(), name = "delete-task"),

]
#########
#######