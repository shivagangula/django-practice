from .setup import *


class UserAuthTest(TestSetUp):
    
    
    def login_view_test(self):
        res = self.client.post(
            self.login_url,
            data={"email": self.email,
                  "password": self.password,
                  },
            format='json')

        login_res = json.loads(res.content)


        self.jwt_access_token = login_res['data']['access']
        self.jwt_refresh_token = login_res['data']['refresh']
         
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.jwt_access_token}')
        
        self.assert_status_code(res= res,fun_name = inspect.stack()[0][3] ,sc= 200)

    
    def refresh_token_view_test(self):
        res = self.client.post(
            self.jwt_refresh_token_url,
            data={"access": self.jwt_access_token,
                  "refresh": self.jwt_refresh_token,
                  },
            format='json')
        
        #self.jwt_access_token = res['data']['access'] 


        self.assert_status_code(res= res,fun_name = inspect.stack()[0][3] ,sc= 200)



     


        