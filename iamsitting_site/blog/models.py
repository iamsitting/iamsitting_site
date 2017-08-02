from django.contrib.auth.models import User
from django.db import models
from django.db.models import permalink
from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse

""" blog models.py
The blog module handles all blog related data
DATA MODELS:
      - Post: Blog post with author, title, content, etc.
      - Comment: Posts mays have comments
      - Category: Blog Category (music, education, sports, etc.)
"""

class Post(models.Model):

  POST_STATUS = (
    ('A', 'Approved'),
    ('P', 'Pending'),
    ('D', 'Denied'),
  )

  author = models.ForeignKey(User)
  title = models.CharField(max_length=100, unique=True)
  slug = models.SlugField(unique=True)
  body = models.TextField()
  status = models.CharField(max_length=1, choices=POST_STATUS, default='P')
  posted_on = models.DateField(db_index=True, auto_now_add=True)
  category = models.ForeignKey('blog.Category')

  def __str__(self):
    return '%s' % self.title

  def get_absolute_url(self):
    return reverse('blog:post', kwargs={'slug': self.slug})

  def get_update_url(self):
    return reverse('blog:edit-post', kwargs={'slug':self.slug})

  def save(self, *args, **kwargs):
    if not self.slug:
      self.slug = slugify(self.title)
    super(Post, self).save(*args, **kwargs) 

class Comment(models.Model):

  COMM_STATUS = (
    ('A', 'Approved'),
    ('P', 'Pending'),
    ('D', 'Denied'),
  )
  name = models.CharField(max_length=40)
  email = models.EmailField(max_length=75)
  text = models.TextField()
  status = models.CharField(max_length=1, choices=COMM_STATUS, default='P')
  post = models.ForeignKey(Post)
  created_on = models.DateTimeField(auto_now_add=True)

  def __unicode__(self):
    return self.text

class Category(models.Model):
  title = models.CharField(max_length=100, primary_key=True, unique=True)
  slug = models.SlugField(unique=True)
  
  def __str__(self):
    return '%s' % self.title
  
  def save(self, *args, **kwargs):
    if not self.slug:
      self.slug = slugify(self.title)
    super(Category, self).save(*args, **kwargs)
