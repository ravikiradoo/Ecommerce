from django.contrib import admin
from .models import Card, Billing_Profile,Payments
# Register your models here.
admin.site.register(Card)
admin.site.register(Billing_Profile)
admin.site.register(Payments)