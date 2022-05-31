from .setup import *


class UserTest(TestSetUp):

    def signup_view_test(self):
        # create user :
        res = self.client.post(
            self.user_signup_url,
            data={"email": self.email,
                  "password": self.password,
                  "password2": self.password,
                  "first_name": self.first_name,
                  "middle_name": self.middle_name,
                  "last_name": self.last_name,
                  "mobile_number": self.mobile_number,
                  },
        )
        
        self.assert_status_code(res= res,fun_name = inspect.stack()[0][3] ,sc= 201)
        
