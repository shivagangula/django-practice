from .setup import *

class ProtectedViewTest(TestSetUp):
       def protected_view_without_auth_test(self):
            res = self.client.get(
                self.protectedview_url,
                format='json')
            
            self.assert_status_code(res= res,fun_name = inspect.stack()[0][3] ,sc= 401)