
from django.contrib import admin
from django.urls import path


from one_class_views.api_view import Empolyee_curd_operation, Empolyee_create_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('employee/<str:uuid>/', Empolyee_curd_operation.as_view(), name="employee_urd"),
    path('employee/', Empolyee_create_list.as_view(),name="employee_lc"),
    
]
