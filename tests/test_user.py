import unittest

from app.models import User

class UserTest(unittest.TestCase):
    def setUp(self):
        self.user_nyanchera = User(username='_nyanchera', password='aaaaaaaa', email='charitynyanchera@gmail.com')
    
    def test_save_user(self):
        self.new_blog.save_post()
        self.assertTrue(len(User.query.all()) > 0)
