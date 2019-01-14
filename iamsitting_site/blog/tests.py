from django.contrib.auth.models import User
from blog.models import Category, Post
from django.test import TestCase
from django.urls import reverse

PW = "badpassword"


class BlogPageTest(TestCase):

  def create_first_user(self, uname):
    first_user = User()
    first_user.username = uname
    first_user.set_password(PW)
    first_user.is_superuser = True
    first_user.save()
    return first_user

  def test_blog_returns_correct_html(self):
    first_user = self.create_first_user('user1')
    self.client.login(username=first_user.username, password=PW)
    response = self.client.get(reverse('blog:new-post'))
    self.assertTemplateUsed(response, 'blog/postform.html')

  def test_can_save_a_POST_request(self):
    first_user = self.create_first_user('user1')
    category = Category(title="History")
    category.save()
    self.client.login(username=first_user.username, password=PW)
    self.client.post(
      reverse('blog:new-post'),
      data={
        'title': 'The Big Title',
        'subtitle': 'A subtitle',
        'body': 'body text',
        'category': category.title})
    self.assertEqual('The Big Title', Post.objects.first().title)


class UserModelTest(TestCase):

  def test_saving_users(self):
    first_user = User()
    first_user.username = "user1"
    first_user.set_password(PW)
    first_user.is_superuser = True
    first_user.save()

    second_user = User()
    second_user.username = "user2"
    second_user.set_password(PW)
    second_user.save()

    users = User.objects.all()
    self.assertEqual(users.count(), 2)
