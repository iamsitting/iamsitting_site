import logging
import re
from datetime import datetime

from django.contrib.auth.models import User
from django.urls import reverse
from django.db import models
from django.template.defaultfilters import slugify

""" blog models.py
The blog module handles all blog related data
DATA MODELS:
      - Post: Blog post with author, title, content, etc.
      - Comment: Posts mays have comments
      - Category: Blog Category (music, education, sports, etc.)
"""
debug = logging.getLogger('debugger')


class Post(models.Model):

  POST_STATUS = (
    ('A', 'Approved'),
    ('P', 'Pending'),
    ('D', 'Denied'),
  )

  author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
  title = models.CharField(max_length=100, unique=True, blank=True, null=True)
  slug = models.SlugField(unique=True, blank=True, null=True)
  body = models.TextField(blank=True)
  status = models.CharField(max_length=1, choices=POST_STATUS, default='P')
  posted_on = models.DateField(db_index=True, auto_now_add=True)
  post_date = models.DateField(blank=True)
  subtitle = models.CharField(max_length=140, blank=True)
  preview = models.CharField(max_length=500, null=True)
  category = models.ForeignKey('blog.Category', null=True, on_delete=models.SET_NULL)

  def __str__(self):
    return '%s' % self.title

  def get_absolute_url(self):
    return reverse('blog:post', kwargs={'slug': self.slug})

  def get_update_url(self):
    return reverse('blog:edit-post', kwargs={'slug': self.slug})

  def get_preview(self):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', self.body)  # remove html tags
    splitted = cleantext.split()[:20]
    preview = ' '.join(splitted) + '...'
    return preview

  def save(self, *args, **kwargs):
    if not self.id:
      self.post_date = datetime.now().date()
    if not self.slug:
      self.slug = slugify(self.title)
    self.preview = self.get_preview()
    super(Post, self).save(*args, **kwargs)


class Comment(models.Model):

  COMM_STATUS = (
    ('A', 'Approved'),
    ('P', 'Pending'),
    ('D', 'Denied'),
  )
  name = models.CharField(max_length=40)
  email = models.EmailField(max_length=75)
  text = models.TextField(blank=True, null=True)
  status = models.CharField(max_length=1, choices=COMM_STATUS, default='P')
  post = models.ForeignKey(Post, blank=True, null=True, on_delete=models.CASCADE)
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


class LocalImage(models.Model):
  file = models.ImageField(upload_to='uploaded_images/')
