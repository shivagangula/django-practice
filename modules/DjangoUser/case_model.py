import logging
from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserManager(BaseUserManager):

    # these method for adding normal user
    def create_user(self, user_type, username, email, password=None):
        if username is None:
            raise TypeError('Users should have a username')
        if email is None:
            raise TypeError('Users should have a Email')

        user = self.model(user_type=user_type, username=username,
                          email=self.normalize_email(email))
        user.set_password(password)
        user.save()
        return user

    # these method for adding super user
    def create_superuser(self, user_type, username, email, password=None):
        if password is None:
            raise TypeError('Password should not be none')

        user = self.create_user(user_type, username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    USER_CHOICES = (('Author', 'Author'),
                    ('Reader', 'Reader'), ('Admin', 'Admin'))

    user_type = models.CharField(max_length=25, choices=USER_CHOICES)
    username = models.CharField(max_length=25)
    email = models.EmailField(_('email'), unique=True)
    password = models.CharField(max_length=100)

    # these field need for default for abstractbase user
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'user_type']

    objects = UserManager()

    def get_username(self):
        return self.username

    def get_user_type(self):
        return self.user_type

    def __str__(self):
        return self.user_type + ' - ' + self.username


class Author(models.Model):
    author_user = models.ForeignKey(
        User, on_delete=models.CASCADE)
    mobile_number = models.BigIntegerField(blank=True, default='0')
    is_verified_email = models.BooleanField(default=False)

    def __str__(self):
        return self.author_user.get_username()


class Reader(models.Model):
    reader_user = models.ForeignKey(
        User, on_delete=models.PROTECT)
    subscriber = models.BooleanField(default=False)
    mobile_number = models.BigIntegerField(default='0')
    is_verified_email = models.BooleanField(default=False)

    def __str__(self):
        return self.reader_user.get_username()


class NewsContent(models.Model):
    writen_by = models.ForeignKey(
        Author, on_delete=CASCADE)
    title = models.CharField(max_length=250)
    content = models.TextField(max_length=25)
    create_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


class NewsTags(models.Model):
    news_title = models.OneToOneField(
        NewsContent, on_delete=models.CASCADE)
    tag = models.CharField(max_length=250)

    def __str__(self):
        return self.tag


# post save signals used for when user created then that user will automatically asigned
# to profile tables

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        try:
            if instance.get_user_type() == 'Author' and instance.get_user_type() != 'Admin':
                Author.objects.create(author_user=instance)
            if instance.get_user_type() == 'Reader' and instance.get_user_type() != 'Admin':
                Reader.objects.create(reader_user=instance)
            if instance.get_user_type() == 'Admin':
                User.objects.create(author_user=instance)
        except Exception as exp:
            print(exp)
