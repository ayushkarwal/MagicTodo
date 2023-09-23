from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import action
from .serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import viewsets
from django.contrib.auth import authenticate


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
        user_name = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username= user_name, password=password)
        if user:
            return Response("User is authenticated", status=200)
        else:
            return Response("User is not found", status=404)