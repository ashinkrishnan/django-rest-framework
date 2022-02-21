from nturl2path import url2pathname
from django.urls import path
from . import views


urlpatterns=[
    path('',views.apiViews, name='api-overview'),
    path('task-list/',views.taskList, name='task-list'),
    path('task-details/<str:pk>/', views.taskDetails, name='task-details'),
    path('task-create/',views.createTask, name='task-create'),
    path('task-update/<str:pk>/', views.updateTask, name='task-update'),
    path('task-delete/<str:pk>/', views.DeleteTask, name='task-delete'),
]