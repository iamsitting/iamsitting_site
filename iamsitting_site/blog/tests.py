from django.contrib.auth.models import User
from blog.models import Category, Post
from django.test import TestCase
from django.urls import reverse

PW = "badpassword"
CATEGORY_TITLE = "History"
NEW_POST_DATA = {
  'title': 'The Big Title',
  'subtitle': 'A subtitle',
  'body': 'body text',
  'category': CATEGORY_TITLE}


def new_user(uname):
  first_user = User()
  first_user.username = uname
  first_user.set_password(PW)
  first_user.is_superuser = True
  first_user.save()
  return first_user


class BlogPageTest(TestCase):

  def test_GET_new_post_template(self):
    user = new_user('user1')
    self.client.login(username=user.username, password=PW)
    response = self.client.get(reverse('blog:new-post'))
    self.assertTemplateUsed(response, 'blog/postform.html')

  def test_POST_new_post_save_post(self):
    user = new_user('user1')
    category = Category(title="History")
    category.save()
    self.client.login(username=user.username, password=PW)
    self.client.post(
      reverse('blog:new-post'),
      data=NEW_POST_DATA)
    self.assertEqual('The Big Title', Post.objects.first().title)

  def test_POST_new_post_redirect(self):
    user = new_user('user1')
    category = Category(title="History")
    category.save()
    self.client.login(username=user.username, password=PW)
    response = self.client.post(
      reverse('blog:new-post'),
      data=NEW_POST_DATA)
    self.assertEqual(response.status_code, 302)
    self.assertEqual(response['location'], reverse('blog:new-post'))


class UserModelTest(TestCase):

  def test_saving_users(self):
    new_user('user1')
    new_user('user2')
    users = User.objects.all()
    self.assertEqual(users.count(), 2)
