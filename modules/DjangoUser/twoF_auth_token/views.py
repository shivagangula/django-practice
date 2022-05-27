from django.shortcuts import render
from modules.DjangoUser.models import User
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .serializer import UserLoginSerializer


class Login(generics.GenericAPIView):
    serializer_class = UserLoginSerializer

    def post(self, request):
        user_serialzer =  self.get_serializer(data= request.data)
        if user_serialzer.is_valid():
            return Response({'data':user_serialzer.data})
        return Response({'error':user_serialzer.errors})

class OTP(generics.GenericAPIView):
    def post(self, request, *args, **kwargs):
        return Response({"ok":"ok"})

class SubmitOTP(generics.GenericAPIView):
    def post(self, request, *args, **kwargs):
        return Response({"ok":"ok"})

class RestrectedViewTest(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        return Response({"ok":"ok"})