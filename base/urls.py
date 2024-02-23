from django.contrib import admin
from django.urls import path,include
# from . import views
from .views import TaskList,TaskDetail

urlpatterns = [
    path('',TaskList.as_view(),name = 'tasks'),
    path('task/<str:pk>/',TaskDetail.as_view(), name = 'task'),

    
]
