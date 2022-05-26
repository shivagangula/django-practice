from django.shortcuts import render
from .models import User, UserProfile
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

class Signup(generics.GenericAPIView):
    def post(self, request, *args, **kwargs):
        return Response({"ok":"ok"})

class Login(generics.GenericAPIView):
    def post(self, request, *args, **kwargs):
        return Response({"ok":"ok"})

class RestrectedViewTest(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        return Response({"ok":"ok"})