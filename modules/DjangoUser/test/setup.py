from rest_framework.test import APITestCase
from django.urls import reverse
from faker import Faker
from modules.DjangoUser.models import User
import json
from colorama import Fore
import colorama
from colorama import init
import traceback
import inspect
import sys




init(autoreset=True)
fake = Faker()


class console:
    def assert_status_code(self, fun_name, res, sc):
        fun_name_len = len(fun_name)
        try:
            original_space = (45 - fun_name_len) * ' '
            self.assertEqual(res.status_code, sc,
                         msg=f"{fun_name} status code wrong")
            print(f"{Fore.GREEN} \u2620 {fun_name} {original_space} : Test Passed !")
        except AssertionError:
            print(f"{Fore.RED} \u2620 {fun_name} {original_space} : Test Faild !")
            print(traceback.format_exc())

            


class TestSetUp(APITestCase, console):
    
    def setUp(self):
        
        # Setup Conifg Variables
        self.email = fake.email()
        self.first_name = 'shiva'
        self.middle_name = 'gangula88'
        self.last_name = 'gag'
        self.mobile_number = '8686573441'
        self.password = "123612543aaa"

        self.jwt_access_token =  None
        self.jwt_refresh_token =  None

        self.user_signup_url = "/user/signup/"
        self.login_url = "/user/jwt_token_cut/login/"
        self.jwt_refresh_token_url = "/user/jwt_token_cut/refresh/"
        self.protectedview_url = '/user/view/'

        return super().setUp()
        
        
# python manage.py test --verbosity=2
