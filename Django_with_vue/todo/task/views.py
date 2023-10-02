from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import action

# Create your views here.
class TaskViewSet(viewsets.ViewSet):
    def list(self, request):
        query_set = Task.objects.all()
        serializer = TaskSerializer(query_set, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        query_set = Task.objects.all()
        task = get_object_or_404(query_set, pk=pk)
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = TaskSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def destroy(self, request, pk=None):
        query_set = Task.objects.all()
        task = get_object_or_404(query_set, pk=pk)
        task.delete()
        return Response(status=204)
    
    def partial_update(self, request, pk=None):
        query_set = Task.objects.all()
        task = get_object_or_404(query_set, pk=pk)
        serializer = TaskSerializer(task, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=200)

