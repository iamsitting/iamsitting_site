from django.contrib.auth.models import User
from blog.models import Category, Post

PW = "badpassword"
CATEGORY_TITLE = "History"
POST_TITLE = 'The Big Title'
POST_SUBTITLE = 'A subtitle'
POST_BODY = 'Here is some text for you.'
NEW_POST_DATA = {
  'title': POST_TITLE,
  'subtitle': POST_SUBTITLE,
  'body': POST_BODY,
  'category': CATEGORY_TITLE}


def new_user(uname, su=False):
  first_user = User()
  first_user.username = uname
  first_user.set_password(PW)
  first_user.is_superuser = su
  first_user.save()
  return first_user


def new_category(title):
  cat = Category(title=title)
  cat.save()
  return cat


def new_post():
  c = new_category(CATEGORY_TITLE)
  data = NEW_POST_DATA.copy()
  data['category'] = c
  p = Post(**data)
  p.save()
  return p
