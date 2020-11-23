from django.db import models

class Education(models.model):
  timespan = models.CharField(max_length=50)
  institution = models.CharField(max_length=50)
  city = models.CharField(max_length=50)
  country = models.CharField(max_length=50)

class Languages(models.model):
  language = models.CharField(max_length=50)
  proficiency = models.CharField(max_length=50)
  comment = models.CharField(max_length=50)

class Education(models.model):
  timespan = models.CharField(max_length=50)
  institution = models.CharField(max_length=50)
  city = models.CharField(max_length=50)
  country = models.CharField(max_length=50)

class Organizations(models.model):
  timespan = models.CharField(max_length=50)
  institution = models.CharField(max_length=50)
  title = models.CharField(max_length=50)
  city = models.CharField(max_length=50)
  country = models.CharField(max_length=50)
  description = models.CharField(max_length=50)

class ProfressionalExperience(models.model):
  timespan = models.CharField(max_length=50)
  institution = models.CharField(max_length=50)
  city = models.CharField(max_length=50)
  country = models.CharField(max_length=50)


class Cv(models.Model):
  name = models.CharField(max_length=50)
  email = models.CharField(max_length=50)
  mobile = models.CharField(max_length=50)
  birthday = models.CharField(max_length=50)
  citizenship = models.CharField(max_length=50)
  github = models.CharField(max_length=50)
  linkedin = models.CharField(max_length=50)
  category = models.ForeignKey(Category, on_delete=models.CASCADE)
# Create your models here.

