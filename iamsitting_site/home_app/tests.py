from django.test import TestCase
from django.urls import reverse


class HomePageTest(TestCase):

  def test_home_returns_correct_html(self):
    response = self.client.get('/')
    self.assertTemplateUsed(response, 'home_app/index.html')


class AboutMeTest(TestCase):

  def test_about_me(self):
    response = self.client.get(reverse('home:about_me'))
    self.assertTemplateUsed(response, 'home_app/about_me.html')


class CVTest(TestCase):

  def test_my_cv(self):
    response = self.client.get(reverse('home:my_cv'))
    self.assertTemplateUsed(response, 'home_app/cv.html')


class CycleXProTest(TestCase):

  def test_cycle_x_pro(self):
    response = self.client.get(reverse('home_app:cycle_x_pro'))
    self.assertTemplateUsed(response, 'home_app/cycle_x_pro.html')


class ContactMeTest(TestCase):

  def test_POST_contact_me(self):
    data = {
      'name': 'tester',
      'email': 'tester@iamsitting.com',
      'message': 'This is a test.'
    }
    response = self.client.post(
        reverse('home_app:contact-me'),
        data=data)
    self.assertEqual(response.status_code, 302)
    self.assertEqual(response['location'], '/')
