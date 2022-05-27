from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import authenticate
from modules.DjangoUser.models import User


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(
            required=True
            )
    password = serializers.CharField(write_only=True, required=True)
    login_status = serializers.BooleanField(default=False, required=False)
    otp_sended_to = serializers.CharField(required=False)
    
    def validate(self, attrs):
        user = authenticate(username = attrs['email'], password = attrs['password'])
        if user is not None:
            attrs['login_status'] = True
            attrs['otp_sended_to'] = 'XXXXXXXX' + str(user.mobile_number)[8:]
            return attrs
        else:
            raise serializers.ValidationError({"login": "Credentials are didn't match."})
    
    
    
                