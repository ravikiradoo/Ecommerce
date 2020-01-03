from django.db import models
from django.utils import timezone
from django.conf import settings
from django.db.models.signals import pre_save
import random
import string

# Create your models here.
USER  = settings.AUTH_USER_MODEL
class Purchase(models.Model):
    user        =  models.ForeignKey(USER, on_delete=models.CASCADE)
    active      = models.BooleanField(default=True)
    shipping_profile=models.IntegerField(null=True)
    card            = models.IntegerField(null=True)
    cart_id         = models.IntegerField(null=True)
