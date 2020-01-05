from django.db import models
from django.conf import settings
from django.urls import reverse
from django.db.models.signals import pre_save
import os

def get_file_name(instance,filename):
    print(instance.id)
    print(filename)
    basename = os.path.basename(filename)
    filename,ext = os.path.splitext(basename)
    filename = 'product_{id}{ext}'.format(id=instance.id,ext=ext)
    final_path = f'product_images/{filename}'
    delete_existing(final_path)
    return final_path

def delete_existing(filename):
    full_path = os.path.join(settings.MEDIA_ROOT,filename)
    if os.path.exists(full_path):
        os.remove(full_path)


# Create your models here.
class Product(models.Model):
    title =         models.CharField(max_length=100)
    description =   models.TextField()
    price =         models.DecimalField(decimal_places=2,max_digits=10,default=0.0,null=False,blank=False)
    image =         models.ImageField(upload_to=get_file_name,blank=True,null=True)
    category =      models.CharField(max_length=100,null=True,blank=True)
    def __str__(self):
        return self.title
    
    def get_product_url(self):
        #return f"/products/product_detail/{self.id}"
        return reverse("products:detail", kwargs={'id':self.id})

class Tag(models.Model):
    tag = models.CharField(max_length=100)
    products = models.ManyToManyField(Product, blank=True)


