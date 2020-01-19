from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager
)
from django.db.models.signals import pre_save,post_save
import stripe
import string
import random
# Create your models here.
user_type= ( ('ADMIN','ADMIN'),
             ('EMPLOYEE','EMPLOYEE'),
             ('CUSTOMER','CUSTOMER'))

class UserManger(BaseUserManager):
    def create_user(self, email, password,is_active=True,is_staff=False,is_admin=False,account_type=None):
        if not email:
            raise ValueError("Please Enter An Email Address")
        if not password:
            raise ValueError("Please Enter Your Password")
        user_obj = self.model(email=self.normalize_email(email))
        if account_type:
            user_obj.account_type = account_type
        else:
            user_obj.account_type='CUSTOMER'
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.active=is_active
        user_obj.set_password(password)
        user_obj.save(using=self._db)
        return user_obj

    def create_staffuser(self, email, password):
       user = self.create_user(email=email,password=password,is_staff=True)
       return user

    def create_superuser(self, email, password):
        user = self.create_user(email=email,password=password,is_staff=True,is_admin=True)
        return user

class User(AbstractBaseUser):
    email = models.EmailField(max_length=300, unique=True)
    key   = models.CharField(max_length=300,unique=True,null=True,blank=True)
    key_exp = models.IntegerField(default=1)
    confirm_email = models.BooleanField(default=False)
    active = models.BooleanField(default=False)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    account_type = models.CharField(default='CUSTOMER',max_length=100, choices=user_type)
    stripe_id = models.CharField(max_length=220,  null=True, blank=True)

    def save(self,*args,**kwargs):
        if self.id is None:
            super(User,self).save(*args,**kwargs)
            self.key = ''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(10,20))) + ''.join(str(random.randint(0,9)) for _ in range(5)) + str(self.id) +''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(10,20)))
        super(User,self).save(*args,**kwargs)
    

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManger()

    def has_perm(self, perm, obj=None):
       return True

    def has_module_perms(self, app_label):
       return True

    @property
    def is_active(self):
        return self.active
    @property
    def is_email_confirmed(self):
        return self.confirm_email

    @property
    def is_admin(self):
        return self.admin
    @property
    def is_staff(self):
        return self.staff

sex = (('MALE','MALE'),('FEMALE','FEMALE'))

class Profile(models.Model):
    user       = models.OneToOneField(User,on_delete=models.CASCADE)
    Name       = models.CharField(max_length=100,null=True,blank=True)
    Sex        = models.CharField(max_length=100,choices=sex,null=True,blank=True)
    phone      = models.CharField(max_length=100,null=True,blank=True)

def get_stripe_id(sender,instance,*args,**kwargs):
    if instance.email is not None and instance.stripe_id is None:
        customer = stripe.Customer.create(email=instance.email)
        instance.stripe_id = customer.id


pre_save.connect(get_stripe_id,sender=User)