from blog.models import Post
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from test.helpers import (CATEGORY_TITLE, NEW_POST_DATA, PW, new_category,
                          new_post, new_user)


class BlogPageTest(TestCase):

  # NewPost

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
    self.assertEqual('The Big Title', Post.objects.first().title)

  def test_POST_new_post_redirect(self):
    user = new_user('user1')
    new_category(CATEGORY_TITLE)
    self.client.login(username=user.username, password=PW)
    response = self.client.post(
      reverse('blog:new-post'),
      data=NEW_POST_DATA)
    self.assertEqual(response.status_code, 302)
    self.assertEqual(response['location'], reverse('blog:new-post'))

  # PostRequests

  def test_GET_post_requests_list(self):
    # This is only for superusers
    suser = new_user('super', su=True)
    new_post()
    self.client.login(username=suser.username, password=PW)
    response = self.client.get(reverse('blog:post-requests'))
    self.assertTemplateUsed(response, 'blog/post_requests.html')
    self.assertIn('The Big Title', response.content.decode())

  # modify_post_status

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


class UserModelTest(TestCase):

  def test_saving_users(self):
    new_user('user1')
    new_user('user2')
    users = User.objects.all()
    self.assertEqual(users.count(), 2)
