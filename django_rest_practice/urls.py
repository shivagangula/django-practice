#from query_test.views import *
from query_test.trans_query import TranscationTestview
from django.contrib import admin
from django.urls import path, include
from one_class_views.models import Empolyee, Department
from one_class_views.serializer import CreateListEmployeeSerializer
from one_class_views.api_view import Empolyee_curd_operation, Empolyee_create_list
from one_class_views.g_views import ( 
    EmpolyeeListCretae, 
    EmployeList,
    EmployeCreate,
    EmployeRetrive
    )

from one_class_views.query_practice import ( 
    EmployeeCountPerDepartmentList,
    FindHighestEmployeeCompany)

from rest_framework import generics

urlpatterns = [
    path('admin/', admin.site.urls),


    # API Views
    path('employee/<str:uuid>/', Empolyee_curd_operation.as_view(), name="employee_urd"),
    path('employee/', Empolyee_create_list.as_view(),name="employee_lc"),
    

    #Concreate Views
    path('gc_lc_employee/', EmpolyeeListCretae.as_view(),name="g_lc_employee_lc"),
    path('gc_l_employee/', EmployeList.as_view(),name="gc_l_employee_lc"),
    path('gc_c_employee/', EmployeCreate.as_view(),name="gc_c_employee_lc"),
    path('gc_r_employee/<str:uuid>/', EmployeRetrive.as_view(),name="gc_r_employee_lc"),
    #path('g_employee/', generics.ListCreateAPIView.as_view(queryset=Empolyee.objects.all(), serializer_class=CreateListEmployeeSerializer), name='user-list')
    

    #query practice
    path('emloyees/department/', EmployeeCountPerDepartmentList.as_view(),name="em_deparment_count"),
    path('emloyees/high/company/', FindHighestEmployeeCompany.as_view(),name="max_company_employee_count"),

   #Transcation Test
    path('trans/', TranscationTestview.as_view(),name="TranscationTestview"),


]
