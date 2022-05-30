from .setup import *
from .user import UserTest
from .jwt import UserAuthTest
from .protected import ProtectedViewTest

class UserOrderTest(UserTest, UserAuthTest, ProtectedViewTest):

    def test_user_order(self):
        self.protected_view_without_auth_test()
        self.signup_view_test()
        self.login_view_test()
        self.refresh_token_view_test()
        


