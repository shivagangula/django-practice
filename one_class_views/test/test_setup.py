from rest_framework.test import APITestCase
from django.urls import reverse
from faker import Faker
from one_class_views.models import Empolyee, Department

fake = Faker()

class TestSetUp(APITestCase):

    def setUp(self):
        self.department_name = "Electrical Engineering"
        department = Department.objects.create(name = self.department_name)
        self.department_uuid = department.uuid

        self.employee_curd_url = "/employee/" 
        self.employee_name = fake.name()
        return super().setUp()