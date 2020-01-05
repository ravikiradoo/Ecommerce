from django.db import models
from django.conf import settings
from products.models import Product
from django.db.models.signals import pre_save,post_save
# Create your models here.
User = settings.AUTH_USER_MODEL

class cart_item(models.Model):
    product =  models.ForeignKey(Product,blank=True, null=True,on_delete=models.SET_NULL)
    quantity = models.IntegerField(null=True)
    total = models.DecimalField(max_digits=10,default=0.0,decimal_places=2)

    def __str__(self):
        return str(self.product.title)+"_"+str(self.id)

class Cart(models.Model):
    user   =   models.ForeignKey(User,blank=True, null=True,on_delete=models.CASCADE)
    total    = models.DecimalField(max_digits=10,default=0.0,decimal_places=2)
    updated   = models.DateTimeField(auto_now=True)
    created   = models.DateTimeField(auto_now_add=True)
    cart_item = models.ManyToManyField(cart_item,null=True)

    def __str__(self):
        return str(self.id)



def cart_pre_save(sender, instance, *args, **kwargs):
    if str(instance) != 'None':
        cart_items = instance.cart_item.all()
        total    = 0
        for c in cart_items:
            total = total + c.total
        
        instance.total = total

def cart_item_pre_save(sender, instance, *args, **kwargs):
    if str(instance) != 'None':
        instance.total = int(instance.quantity ) * instance.product.price

pre_save.connect(cart_pre_save,sender=Cart)
pre_save.connect(cart_item_pre_save,sender=cart_item)
    
    
