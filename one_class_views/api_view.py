# APIVIEW
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Department, Empolyee
from .serializer import DepartmentSerializer, EmployeeSerializer,CreateListEmployeeSerializer
from rest_framework import status
from .renders import SerializerDataRender

"""
    REST framework provides an APIView class, which subclasses Django's View class.
"""


class Empolyee_curd_operation(APIView):
    """ 
    its provide single employee info
    its provide single employee info update
    its provide single employee info delete

    """
    # authentication_classes = None
    # permission_classes = None
    renderer_classes = [SerializerDataRender]
    # parser_classes = None
    # authentication_classes = None
    # throttle_classes = None
    # permission_classes = None
    # content_negotiation_class = None

    def get_object(self, uuid):
        try:
            return Empolyee.objects.get(uuid=uuid)
        except Empolyee.DoesNotExist:
            return Response({"status":"failed"}, status= status.HTTP_404_NOT_FOUND)

    def get(self, request, uuid, format=None):
        employee = self.get_object(uuid)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)

    def put(self, request, uuid, format=None):
        employee = self.get_object(uuid)
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, uuid, format=None):
        employee = self.get_object(uuid)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class Empolyee_create_list(APIView):

    """
    its providing list employees
    create new employee
    """
    renderer_classes = [SerializerDataRender]
    
    def get(self, request, format=None):
        empolyee = Empolyee.objects.all()
        serializer = CreateListEmployeeSerializer(empolyee, many=True)
        return Response(serializer.data)


    def post(self, request, format=None):
        serializer = CreateListEmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)