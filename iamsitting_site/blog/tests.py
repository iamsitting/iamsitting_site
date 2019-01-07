from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class BlogPageTest(TestCase):

  def test_blog_returns_correct_html(self):
    first_user = User()
    first_user.username = "user1"
    first_user.password = 'password1'
    first_user.is_superuser = True
    first_user.save()

    self.client.login(username=first_user.username, password=first_user.password)
    response = self.client.get(reverse('blog:new-post'))
    self.assertTemplateUsed(response, 'blog/postform.html')


class UserModelTest(TestCase):

  def test_saving_users(self):
    first_user = User()
    first_user.username = "user1"
    first_user.password = 'password1'
    first_user.is_superuser = True
    first_user.save()

    second_user = User()
    second_user.username = "user2"
    second_user.password = "password2"
    second_user.save()

    users = User.objects.all()
    self.assertEqual(users.count(), 2)
