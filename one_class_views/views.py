

# Generic views
from rest_framework import generics
from .models import Department, Empolyee
from .serializer import DepartmentSerializer, EmployeeSerializer
class normal_generic_view(generics.GenericAPIView):
    """
    The generic views provided by REST framework allow you
    to quickly build API views that map closely to your database models.
    """
    queryset = Empolyee.objects.all()
    def get(self):
        pass

