from django.db import models
from products.models import Product
from billing_profile.models import Billing_Profile
from shipping_profile.models import Shipping_Profile
from django.conf import settings
from django.db.models.signals import pre_save
from django.utils import timezone
import string
import random
import decimal
# Create your models here.
User = settings.AUTH_USER_MODEL
Order_Status = (
    ('ordered','Ordered'),
    ('shipped','Shipped'),
    ('delivered','Delivered'),
    ('returned','Returned'),
    ('refunded','Refunded')
)

class order_item(models.Model):
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,null=True,blank=True)
    quantity = models.IntegerField()
    total = models.DecimalField(max_digits=10,default=0.0,decimal_places=2)

class Orders(models.Model):
    user            = models.ForeignKey(User,blank=True, null=True,on_delete=models.SET_NULL)
    order_id        = models.CharField(max_length=25,unique=True, null=True,blank=True)
    order_item       = models.ManyToManyField(order_item,null=True,blank=True)
    order_status    = models.CharField(max_length=20,choices=Order_Status)
    created         = models.DateTimeField(auto_now_add=True)
    updated         = models.DateTimeField(auto_now=True)
    total           = models.DecimalField(max_digits=10,default=0.0,decimal_places=2)
    shipping        = models.DecimalField(max_digits=10,default=40.0,decimal_places=2)
    billing_profile = models.ForeignKey(Billing_Profile,on_delete=models.SET_NULL,null=True)
    shipping_proile = models.ForeignKey(Shipping_Profile,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.order_id

def order_pre_save(sender,instance, *args, **kwargs):
    
    if instance.order_id is None:
        timestamp   =  timezone.now().strftime('%Y%m%d%H%M%S%f')
        instance.order_id =   'O'+''.join(random.choice(string.ascii_uppercase) for _ in range(4))+timestamp
    instance.total = decimal.Decimal(instance.total) + decimal.Decimal(instance.shipping)


pre_save.connect(order_pre_save,sender=Orders)

