from .models import User
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all(), message="Email already exsited")]
            )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    first_name = serializers.CharField(max_length=25, required=True)
    middle_name = serializers.CharField(max_length=25, required=True)
    last_name = serializers.CharField(max_length=25, required=True)
    mobile_number = serializers.IntegerField(required=True, validators=[UniqueValidator(queryset=User.objects.all(), message="Mobile already exsited")] )
    is_premium = serializers.BooleanField(default=False, required=False)

    class Meta:
        model = User
        fields = [
            'email',
            'mobile_number',
            'first_name',
            'middle_name',
            'last_name',
            'mobile_number',
            'is_premium',
            'password',
            'password2'
        ]
        

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        if len( str(attrs['mobile_number']) ) != 10:
            raise serializers.ValidationError({"mobile_number": "mobile_number length invalid"})
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email'],
            middle_name=validated_data['middle_name'],
            first_name = validated_data['first_name'],
            last_name=validated_data['last_name'],
            mobile_number=validated_data['mobile_number']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

