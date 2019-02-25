from django.db import models


class Patient(models.Model):

  firstname = models.CharField(max_length=100, blank=True, null=True)
  lastname = models.CharField(max_length=100, blank=True, null=True)
  age = models.PositiveSmallIntegerField(default=0)
  weight = models.PositiveSmallIntegerField(default=0)
  height = models.PositiveSmallIntegerField(default=0)
  creatinine = models.PositiveSmallIntegerField(default=0)
  dose = models.PositiveSmallIntegerField(default=0)
  frequency = models.PositiveSmallIntegerField(default=0)

  def __str__(self):
    return '%s %s' % (self.firstname, self.lastname)
