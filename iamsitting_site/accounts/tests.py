from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class LoginPageTest(TestCase):

  def test_login_returns_correct_html(self):
    response = self.client.get(reverse('accounts:login'))
    self.assertTemplateUsed(response, 'registration/login.html')


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
