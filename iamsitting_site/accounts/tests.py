from django.test import TestCase
from django.urls import reverse


class HomePageTest(TestCase):

  def test_login_returns_correct_html(self):
    response = self.client.get(reverse('accounts:login'))
    self.assertTemplateUsed(response, 'registration/login.html')
