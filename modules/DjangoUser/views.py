from django.shortcuts import render
from .models import User
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .serializer import UserSerializer
from modules.DrfRenders.renders import SerializerDataRender
from rest_framework import generics
from rest_framework.permissions import AllowAny



# Both view are valid
class Signup2(generics.GenericAPIView):

    serializer_class = UserSerializer
    renderer_classes = [SerializerDataRender]

    def post(self, request, *args, **kwargs):
        user_serializer =  UserSerializer(data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response({'data':user_serializer.data})
        else:
            return Response({'data':user_serializer.errors})



class Signup(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer
    renderer_classes = [SerializerDataRender]