from django.db import models

# we can create or extend custom django models
# one to one 
# abstract user
# abstract base
import logging
from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

import uuid


class UserManager(BaseUserManager):

    # these method for adding normal user
    def create_user(self, email, password=None):
       
        if email is None:
            raise TypeError('Users should have a Email')

        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save()
        return user

    # these method for adding super user
    def create_superuser(self, email, password=None):
        if password is None:
            raise TypeError('Password should not be none')

        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    email = models.EmailField(_('email'), unique=True)
    password = models.CharField(max_length=100)

    # these field need for default for abstractbase user
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()


    def __str__(self):
        return str(self.uuid)


class UserProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    first_name = models.CharField(max_length=25)
    middle_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    mobile_number = models.IntegerField()
    is_premium = models.BooleanField(default=False)
   
    




#CUSTOM USER MIGRATION ISSUE
#------------------------------
# create tabls 1st
# makemigrations 
# add AUTH_TABLE_MODEL in settings
# comment admin app in settings, urls 
# run migrations
# un comment everything