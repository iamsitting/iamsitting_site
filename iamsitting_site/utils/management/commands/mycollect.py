import os

from django.core.management.base import BaseCommand


class Command(BaseCommand):

  exclude = [
    'admin',
    'tiny_mce',
    'rest_framework',
    'django_tinymce',
    'django_extensions',
  ]

  command_string = 'python manage.py collectstatic --no-input'

  def handle(self, *args, **options):

    print('Not collecting...')
    for module in self.exclude:
      print(module)
      self.command_string += ' -i ' + module

    os.system(self.command_string)
