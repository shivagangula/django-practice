from django.urls import path
from .views import Signup
from .auth_types.views import (
    TokenLogin,
    JWTLogin, 
    JWTtokenRefresh,
    JWTLogout,
    RestrectedViewTest)

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
    
app_name = 'DjangoUser'

urlpatterns = [
    path('view/', RestrectedViewTest.as_view()),
    path('signup/', Signup.as_view()),
    path('token/login/', TokenLogin.as_view()),
    
    
    path('jwt_native/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('jwt_native/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    path('jwt_token_cut/login/', JWTLogin.as_view()),
    path('jwt_token_cut/refresh/', JWTtokenRefresh.as_view()),
    path('jwt_token_cut/logout/', JWTLogout.as_view()),
]