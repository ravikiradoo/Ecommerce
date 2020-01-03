from django.db import models
from django.conf import settings
from addresses.models import Address
from django.db.models.signals import pre_save
import stripe

stripe.api_key = 'sk_test_8FspIcfPQB72KzJnfwXM2GXj00G7rH0TK5'
# Create your models here.
User = settings.AUTH_USER_MODEL

Cart_Type = (
                ('debit','Debit'),
                ('credit','Credit')
)



class Billing_Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    First_Name = models.CharField(max_length=100)
    Last_Name  = models.CharField(max_length=100)
    Email      = models.CharField(max_length=100)
    Phone      = models.CharField(max_length=25) 
    Address = models.ForeignKey(Address,on_delete=models.SET_NULL,null=True)
    stripe_id = models.CharField(max_length=220,  null=True, blank=True)
    
class Card(models.Model):
    Billing_Profile = models.ForeignKey(Billing_Profile,on_delete=models.CASCADE)
    stripe_id = models.CharField(max_length=100)
    Month  = models.IntegerField()
    Year   = models.IntegerField()
    brand   = models.CharField(max_length=100)
    last4   = models.CharField(max_length=4)

class Payments(models.Model):
    order_id = models.CharField(max_length=25,unique=True, null=True,blank=True)
    paid     =  models.BooleanField(default=False)
    amount   =  models.DecimalField(max_digits=10,default=0.0,decimal_places=2)
    created  =  models.DateTimeField(auto_now_add=True)
    payement_method = models.CharField(max_length=100)
    stripe_id = models.CharField(max_length=100,null=True)



def get_stripe_id(sender,instance,*args,**kwargs):
    if instance.Email is not None and instance.stripe_id is None:
        customer = stripe.Customer.create(email=instance.Email)
        instance.stripe_id = customer.id

pre_save.connect(get_stripe_id,sender=Billing_Profile)




