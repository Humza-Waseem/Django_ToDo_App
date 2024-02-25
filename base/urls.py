from django.contrib import admin
from django.urls import path,include
# from . import views
from .views import TaskList,TaskDetail,TaskCreate,EditTask,DeleteTask

urlpatterns = [
    path('',TaskList.as_view(),name = 'tasksHome'),
    path('task/<str:pk>/',TaskDetail.as_view(), name = 'task'),
    path('create-task/',TaskCreate.as_view(), name = "create-task"),
    path('edit-task/<str:pk>/',EditTask.as_view(), name = "edit-task"),
    path('deleteTask/<str:pk>/',DeleteTask.as_view(), name = "delete-task"),


    
]
