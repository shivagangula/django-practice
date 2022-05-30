from django.shortcuts import render
from modules.DjangoUser.models import User
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .serializer import UserTokenLoginSerializer, UserJWTLoginSerializer
from rest_framework.permissions import (
    IsAuthenticated,
)
from rest_framework.authentication import (
    TokenAuthentication,
)
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from modules.DrfRenders.renders import SerializerDataRender

# Token Auth
class TokenLogin(generics.GenericAPIView):
    serializer_class = UserTokenLoginSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        user_serialzer =  self.get_serializer(data= request.data)
        if user_serialzer.is_valid():
            return Response({'data':user_serialzer.data})
        return Response({'error':user_serialzer.errors})


# Oauth
class JWTLogin(TokenObtainPairView):
    renderer_classes  = [SerializerDataRender]

class JWTtokenRefresh(TokenRefreshView):
    renderer_classes  = [SerializerDataRender]


class JWTLogout(generics.GenericAPIView):

    "https://medium.com/django-rest/logout-django-rest-framework-eb1b53ac6d35"
    
    authentication_classes = [JWTAuthentication]

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response({"status":"succuss"},status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            print(e)
            return Response({"status":"succuss"},status=status.HTTP_400_BAD_REQUEST)


class RestrectedViewTest(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    #authentication_classes = [TokenAuthentication]
    authentication_classes = [JWTAuthentication]

    renderer_classes  = [SerializerDataRender]
    def get(self, request, *args, **kwargs):
        return Response({"status":"succuss"})