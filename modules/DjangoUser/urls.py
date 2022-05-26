from django.urls import path
from .views import Signup, Login, RestrectedViewTest
    
app_name = 'DjangoUser'

urlpatterns = [
    path('signup/', Signup.as_view()),
    path('login/', Login.as_view()),
    path('view/', RestrectedViewTest.as_view()),
]