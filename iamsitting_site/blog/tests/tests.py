from blog.models import Post
from blog.tests.helpers import (CATEGORY_TITLE, NEW_POST_DATA, PW,
                                new_category, new_post, new_user)
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class NewPostTest(TestCase):

  def test_GET_new_post_template(self):
    user = new_user('user1')
    self.client.login(username=user.username, password=PW)
    response = self.client.get(reverse('blog:new-post'))
    self.assertTemplateUsed(response, 'blog/postform.html')

  def test_POST_new_post_save_post(self):
    user = new_user('user1')
    new_category(CATEGORY_TITLE)
    self.client.login(username=user.username, password=PW)
    self.client.post(
      reverse('blog:new-post'),
      data=NEW_POST_DATA)
    self.assertEqual(NEW_POST_DATA['title'], Post.objects.first().title)

  def test_POST_new_post_redirect(self):
    user = new_user('user1')
    new_category(CATEGORY_TITLE)
    self.client.login(username=user.username, password=PW)
    response = self.client.post(
      reverse('blog:new-post'),
      data=NEW_POST_DATA)
    self.assertEqual(response.status_code, 302)
    self.assertEqual(response['location'], reverse('blog:new-post'))


class EditPostTest(TestCase):

  def test_GET_edit_post_template(self):
    suser = new_user('super', su=True)
    p = new_post()
    self.client.login(username=suser.username, password=PW)
    response = self.client.get(p.get_update_url())
    self.assertTemplateUsed(response, 'blog/postform.html')
    self.assertIn(p.title, response.content.decode())

  def test_POST_edit_post(self):
    suser = new_user('super', su=True)
    p = new_post()
    self.client.login(username=suser.username, password=PW)
    data = {
      'title': p.title,
      'subtitle': p.subtitle,
      'body': "This a new body.",
      'category': p.category
    }
    self.client.post(p.get_update_url(), data=data)
    self.assertNotEqual(p.body, Post.objects.get(id=p.id).body)

  def test_POST_edit_post_redirect(self):
    suser = new_user('super', su=True)
    p = new_post()
    self.client.login(username=suser.username, password=PW)
    data = {
      'title': p.title,
      'subtitle': p.subtitle,
      'body': "This a new body.",
      'category': p.category
    }
    response = self.client.post(p.get_update_url(), data=data)
    self.assertEqual(response.status_code, 302)
    self.assertEqual(response['location'], reverse('blog:new-post'))


class PostRequestsTest(TestCase):

  def test_GET_post_requests_list(self):
    # This is only for superusers
    suser = new_user('super', su=True)
    p = new_post()
    self.client.login(username=suser.username, password=PW)
    response = self.client.get(reverse('blog:post-requests'))
    self.assertTemplateUsed(response, 'blog/post_requests.html')
    self.assertIn(p.title, response.content.decode())


class ModifyPostStatusTest(TestCase):

  def test_GET_modify_post_status(self):
    # This is only for supersusers
    suser = new_user('super', su=True)
    p = new_post()
    self.client.login(username=suser.username, password=PW)
    kwargs = {
      'status': 'D',
      'id': p.id
    }
    self.client.get(reverse('blog:modify-post-status', kwargs=kwargs))
    self.assertEquals(Post.objects.get(id=p.id).status, 'D')


class ViewPostTest(TestCase):

  def test_GET_view_post_template(self):
    p = new_post()
    response = self.client.get(p.get_absolute_url())
    self.assertTemplateUsed(response, 'blog/view_post.html')
    self.assertIn(p.title, response.content.decode())


class UserModelTest(TestCase):

  def test_saving_users(self):
    new_user('user1')
    new_user('user2')
    users = User.objects.all()
    self.assertEqual(users.count(), 2)
