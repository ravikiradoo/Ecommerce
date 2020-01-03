from django.db import models
from django.conf import settings
from addresses.models import Address
# Create your models here.
User = settings.AUTH_USER_MODEL

class Shipping_Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    First_Name = models.CharField(max_length=100)
    Last_Name  = models.CharField(max_length=100)
    Email      = models.CharField(max_length=100)
    Phone      = models.CharField(max_length=25) 
    Address = models.ForeignKey(Address,on_delete=models.SET_NULL,null=True)
