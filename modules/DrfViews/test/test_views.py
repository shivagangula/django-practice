from .test_setup import TestSetUp
from modules.DrfViews.models.basic_models import Empolyee, Department
import json


class TestViews(TestSetUp):

    def test_get_all_employees(self):
        res = self.client.get(self.employee_curd_url)
        self.assertEqual(res.status_code, 200, msg="Status Code Missmatch")  


    


