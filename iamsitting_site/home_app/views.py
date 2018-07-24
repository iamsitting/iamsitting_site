import logging

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render

from blog.models import Post

debug = logging.getLogger('debugger')
# Create your views here.


def home(request):
  FEATURED_SLUG = 'the-roman-empire'  # TODO: Add this feature on front-end
  featured_post = None
  all_posts = Post.objects.filter(status='A').order_by('-post_date')
  posts = None
  ctx = {}
  if len(all_posts) > 0:
    if all_posts.filter(slug=FEATURED_SLUG).exists():
      featured_post = all_posts.get(slug=FEATURED_SLUG)
    else:
      featured_post = all_posts.first()

    all_posts = all_posts.exclude(pk=featured_post.pk)  # len is less one

    if len(all_posts) > 0:
      paginator = Paginator(all_posts, 6)
      page = request.GET.get('page')
      try:
        posts = paginator.page(page)
      except PageNotAnInteger:
        posts = paginator.page(1)
      except EmptyPage:
        posts = paginator.page(paginator.num_pages)

  ctx['featured_post'] = featured_post
  ctx['posts'] = posts
  return render(request, 'home_app/index.html', context=ctx)


def about_me(request):
  return render(request, 'home_app/about_me.html')


def my_cv(request):
  return render(request, 'home_app/cv.html')


def cycle_x_pro(request):
  return render(request, 'home_app/cycle_x_pro.html')
