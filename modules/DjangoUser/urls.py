from django.urls import path
from .views import Signup
from .twoF_auth_token.views import (Login, 
RestrectedViewTest,OTP, SubmitOTP)
    
app_name = 'DjangoUser'

urlpatterns = [
    path('signup/', Signup.as_view()),
    path('login/', Login.as_view()),
    path('view/', RestrectedViewTest.as_view()),
    path('otp/', OTP.as_view()),
]