import logging
from datetime import datetime

from django.core.mail import send_mail
from django.shortcuts import render
from django.http import HttpResponse

debug = logging.getLogger('debugger')


def home(request):
  return render(request, 'home_app/about_me.html')


def my_cv(request):
  return render(request, 'home_app/cv.html')


def cycle_x_pro(request):
  return render(request, 'home_app/cycle_x_pro.html')


def contact_me(request):
  if request.method == 'POST':
    name = request.POST.get('name')
    email = request.POST.get('email')
    message = 'This is message from iamsitting.com.\n ----\n' + request.POST.get('message')
    subject = 'From: ' + name + ' at ' + str(datetime.now())
    send_mail(subject, message, email, ['carlos@iamsitting.com'], fail_silently=False)
    return HttpResponse('Success', status=200)
