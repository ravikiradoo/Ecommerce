from django.db import models

# Create your models here.

class Address(models.Model):
    Address  =  models.CharField(max_length=200)
    City     =  models.CharField(max_length=100)
    State    =  models.CharField(max_length=100)
    Country  =  models.CharField(max_length=100)
    zipcode  =  models.CharField(max_length=100)

