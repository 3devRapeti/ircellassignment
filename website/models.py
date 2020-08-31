from django.db import models

# Create your models here.
class profiles(models.Model):
    source = models.CharField(max_length=250)
    name = models.CharField(max_length=50)
    dept = models.CharField(max_length=250)
    place = models.CharField(max_length=350)
    rsch = models.CharField(max_length=500)
    dur = models.CharField(max_length=50)
