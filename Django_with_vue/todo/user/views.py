from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import action
from .serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import viewsets
from django.contrib.auth import authenticate
from task.models import Task
from task.serializers import TaskSerializer


class UserView(viewsets.ViewSet):

    def list(self, request):
        query_set = User.objects.all()
        serializer = UserSerializer(query_set, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)
    
    @action(detail=False, methods=['post'])
    def log_in(self, request):
        result = {"status":True, "msg": ""}
        user_name = request.data.get("username")
        password = request.data.get("password")
        user_match, pass_match = self.authenticate_user(username= user_name, password=password)
        if user_match and pass_match:
            result["msg"] = "User is authenticated"
            try:
                user = User.objects.get(username=user_name, password=password)
                user_serializer = UserSerializer(user)
            except User.DoesNotExist:
                result["status"] = False
                result["msg"] = "User is not found"
                return Response(result, status=404)
            return Response(user_serializer.data, status=200)
        elif user_match:
            result["status"] = False
            result["msg"] = "Wrong password"
            return Response(result, status=400)
        else:
            result["status"] = False
            result["msg"] = "User is not found"
            return Response(result, status=404)
    
    def authenticate_user(self, username, password):
        user_match, pass_match = False, False
        try:
            user = User.objects.get(username = username)
            user_match = True
            return (user_match, True) if user.password == password else (user_match, False)
        except User.DoesNotExist:
            return (user_match, pass_match)
    
    @action(detail=True, methods=["GET"])
    def get_tasks(self, request, pk=None):
        query_set = Task.objects.filter(created_by = pk).order_by('completed_on')
        serializer = TaskSerializer(query_set, many=True)
        return Response(serializer.data)
