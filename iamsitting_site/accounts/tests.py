from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class LoginPageTest(TestCase):

  def test_login_returns_correct_html(self):
    response = self.client.get(reverse('accounts:login'))
    self.assertTemplateUsed(response, 'registration/login.html')


class SignUpPageTest(TestCase):

  def test_signup_returns_correct_html(self):
    response = self.client.get(reverse('accounts:signup'))
    self.assertTemplateUsed(response, 'accounts/signup.html')

  def test_POST_signup(self):
    data = {
      'username': 'tester',
      'email': 'tester@iamsitting.com',
      'password': 'testpassword'
    }
    response = self.client.post(
        reverse('accounts:signup'),
        data=data)
    self.assertEqual(response.status_code, 200)


class UserModelTest(TestCase):

  def test_saving_users(self):
    first_user = User()
    first_user.username = "user1"
    first_user.password = 'badpassword'
    first_user.is_superuser = True
    first_user.save()

    second_user = User()
    second_user.username = "user2"
    second_user.password = "badpassword"
    second_user.save()

    users = User.objects.all()
    self.assertEqual(users.count(), 2)
