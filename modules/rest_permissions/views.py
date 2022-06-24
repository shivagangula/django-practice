from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import (
    IsAuthenticated,
)
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication


from rest_framework import permissions

class PremiumUser(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_premium:
            return True


class CustomPermissionTest(generics.GenericAPIView):
    permission_classes = [PremiumUser & IsAuthenticated]
    authentication_classes = [JWTAuthentication]


    def get(self, request, *args, **kwargs):
        return Response({'status': 'succuss'}, status=200)
