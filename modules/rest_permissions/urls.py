from .views import CustomPermissionTest
from django.urls import path

    
app_name = 'rest_permissions'

urlpatterns = [
   
    path('test/', CustomPermissionTest.as_view()),
]