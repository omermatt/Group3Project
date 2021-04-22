from django.test import TestCase, Client
from .models import MyUser


# Tests for login
class LoginTest(TestCase):
    def setUp(self):
        self.Client = Client()
        self.user1 = MyUser(name='user1', password='password')
        self.user1.save()

    # test for correct name and password
    def testCorrect(self):
        response = self.Client.post('/', {'username': 'user1', 'password': 'password'})
        self.assertTrue(response.url, 'Username and password are correct')

    # test for not existed name
    def test_WrongName(self):
        response = self.Client.post('/', {'username': 'wrong', 'password': 'password'})
        self.assertFalse(response.context["username"], 'Username not found')

    # test for wrong password
    def test_WrongPassword(self):
        response = self.Client.post('/', {'username': 'user1', 'password': 'wrong'})
        self.assertFalse(response.context["password"], 'Password is incorrect')

    # test for null name
    def test_NullName(self):
        response = self.Client.post('/', {'username': '', 'password': 'password'})
        self.assertFalse(response.context["username"], 'Username cannot be empty')

    # test for null password
    def test_NullPassword(self):
        response = self.Client.post('/sign in/', {'username': 'user1', 'password': ''})
        self.assertFalse(response.context["password"], 'Password cannot be empty')

# Xin part of the unit test is above.

