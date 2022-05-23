# Generic views
from rest_framework import generics
from modules.DrfViews.models.basic_models import Department, Empolyee, Company
from modules.DrfViews.serializers.basic_serializer import (
     DepartmentSerializer, CompanySerializer, CreateListEmployeeSerializer, EmployeeSerializer )
from rest_framework import generics
from django.db.models import Count
from rest_framework.response import Response
from modules.DrfRenders.renders import SerializerDataRender





class EmployeeCountPerDepartmentList(generics.ListAPIView):
    """
    Get Number of employees per departments
    """
    renderer_classes = [SerializerDataRender]
    queryset = Department.objects.annotate(
        no_of_employes = Count('employees'))
    serializer_class = DepartmentSerializer
    

class FindHighestEmployeeCompany(generics.GenericAPIView):
    """
    Get Company which is highest employees
    """
    renderer_classes = [SerializerDataRender]
    serializer_class = CompanySerializer
    queryset = Company.objects.all().annotate(emp =  Count('company__employees')).order_by('-emp').first()
    
    def get(self, request, *args, **kwargs):
        instance = self.get_queryset()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


 