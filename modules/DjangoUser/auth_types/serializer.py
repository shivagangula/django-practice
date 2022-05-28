from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import authenticate
from modules.DjangoUser.models import User
from rest_framework.authtoken.models import Token
from django.utils import timezone
from rest_framework_simplejwt.tokens import RefreshToken


class UserTokenLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(
            required=True
            )
    password = serializers.CharField(write_only=True, required=True)
    login_status = serializers.BooleanField(default=False, required=False)
    otp_sended_to = serializers.CharField(required=False)
    token = serializers.CharField(required=False)
    
    def validate(self, attrs):
        user = authenticate(username = attrs['email'], password = attrs['password'])
        if user is not None:
            attrs['login_status'] = True
            attrs['otp_sended_to'] = 'XXXXXXXX' + str(user.mobile_number)[8:]

            token, created = Token.objects.get_or_create(user=user)
            if not created:
                token.created = timezone.now()
                token.save()
                attrs['token'] = token
            attrs['token'] = token
            return attrs
        else:
            raise serializers.ValidationError({"login": "Credentials are didn't match."})
    
    
class UserJWTLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(
            required=True, write_only=True
            )
    password = serializers.CharField(write_only=True, required=True)
    access_token = serializers.CharField(required=False)
    refresh_token = serializers.CharField(required=False)
    
    def validate(self, attrs):
        user = authenticate(username = attrs['email'], password = attrs['password'])
        if user is not None:
            
            # custom send jwt tokens in serializer
            jwt_tokens = RefreshToken.for_user(user)
            attrs['refresh_token'] =  str(jwt_tokens)
            attrs['access_token'] = str(jwt_tokens.access_token)

            return attrs
        else:
            raise serializers.ValidationError({"login": "Credentials are didn't match."})

