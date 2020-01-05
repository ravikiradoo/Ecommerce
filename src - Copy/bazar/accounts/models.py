from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager
)
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
    active = models.BooleanField(default=False)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    account_type = models.CharField(default='CUSTOMER',max_length=100, choices=user_type)

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
    def is_admin(self):
        return self.admin
    @property
    def is_staff(self):
        return self.staff
    