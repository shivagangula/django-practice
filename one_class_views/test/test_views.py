from .test_setup import TestSetUp
from one_class_views.models import Empolyee, Department
import json


class TestViews(TestSetUp):

    def test_get_all_employees(self):
        res = self.client.get(self.employee_curd_url)
        self.assertEqual(res.status_code, 200, msg="Status Code Missmatch")

    def test_create_employee(self):
        res = self.client.post(
            self.employee_curd_url,
            data={"name": self.employee_name,
                  "department_uuid": self.department_uuid},
            format='json')
        res_data = json.loads(res.content)
        res_department_uuid = res_data['data']['department']['uuid']
        self.assertEqual(res.status_code, 201, msg="Status Code Missmatch")
        self.assertEqual(res_department_uuid,
                         self.department_uuid, msg="Department UUID mismatch")
        self.assertEqual(res_data['data']['department']['name'],
                         self.employee_name, msg="emplooyee name mismatch")
