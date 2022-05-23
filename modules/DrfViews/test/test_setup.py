from rest_framework.test import APITestCase
from django.urls import reverse
from faker import Faker
from modules.DrfViews.models.basic_models import Empolyee, Department
import json

fake = Faker()

class TestSetUp(APITestCase):

    def setUp(self):

        # Create Department :
        self.department_name = "Electrical Engineering"
        department = Department.objects.create(name = self.department_name)
        self.department_uuid = str ( department.uuid )

        self.employee_curd_url = "/employee/" 
        self.employee_name = fake.name()
        
        
        # Create Employee : 
        res = self.client.post(
            self.employee_curd_url,
            data={"name": self.employee_name,
                  "department_uuid": self.department_uuid},
            format='json')
        res_data = json.loads(res.content)
        res_department_uuid = res_data['data']['department']['uuid']

        self.assertEqual(res.status_code, 201, msg="Status Code Missmatch") #case : check status code
        self.assertEqual(res_department_uuid,
                         self.department_uuid, msg="Department UUID mismatch")  #case : check employee uuid
        self.assertEqual(res_data['data']['name'],
                         self.employee_name, msg="emplooyee name mismatch")  #case : check  employee
        self.employee_uuid = res_data['data']['uuid']


        return super().setUp()




# python manage.py test --verbosity=2