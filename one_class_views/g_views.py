# Generic views
from rest_framework import generics
from .models import Department, Empolyee
from .serializer import DepartmentSerializer, EmployeeSerializer
from rest_framework import generics
from one_class_views.serializer import CreateListEmployeeSerializer, EmployeeSerializer
from .renders import SerializerDataRender
from django.db.models import Count


# Concreate Views
class EmployeRetrive(generics.RetrieveAPIView):
    """
    Used for read-only endpoints to represent a single model instance.
    Provides a get method handler.
    Extends: GenericAPIView, RetrieveModelMixin
    """
    renderer_classes = [SerializerDataRender]
    queryset = Empolyee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = "uuid"

class EmployeCreate(generics.CreateAPIView):
    """
    Used for create-only endpoints.
    Provides a post method handler.
    Extends: GenericAPIView, CreateModelMixin
    """
    renderer_classes = [SerializerDataRender]
    queryset=Empolyee.objects.all()
    serializer_class=CreateListEmployeeSerializer



class EmployeList(generics.ListAPIView):
    """
    Used for read-only endpoints to represent a collection of model instances.
    Provides a get method handler.
    Extends: GenericAPIView, ListModelMixin
    """
    renderer_classes = [SerializerDataRender]
    queryset=Empolyee.objects.all()
    serializer_class=CreateListEmployeeSerializer



class EmpolyeeListCretae(generics.ListCreateAPIView):
    """
    Used for read-write endpoints to represent a collection of model instances.
    Provides get and post method handlers. 
    Extends: GenericAPIView, ListModelMixin, CreateModelMixin
    """
    renderer_classes = [SerializerDataRender]
    queryset=Empolyee.objects.all()
    serializer_class=CreateListEmployeeSerializer
 


