from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from.serializers import TaskSerializrers

from .models import Task

# Create your views here.

@api_view(['GET'])
def apiViews(request):
    api_urls = {
        'List' : '/task-list/',
        'Details':'/task-detail/<str:pk>/',
        'Delete':'/task-delete/<str:pk>/',
        'Create':'/task-create/',
        'Update':'/task-update/<str:pk>/',
    }
    return JsonResponse(api_urls)

@api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all()
    serializer = TaskSerializrers(tasks,many=True)
    return Response(serializer.data)


@api_view(['GET'])
def taskDetails(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializrers(task,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createTask(request):
    serializer = TaskSerializrers(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        pass

    return Response(serializer.data)

@api_view(['POST'])
def updateTask(request,pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializrers(instance=task,data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def DeleteTask(request,pk):
    task = Task.objects.get(id=pk)
    task.delete()
    
    return Response('item deleted succesesfully...')

