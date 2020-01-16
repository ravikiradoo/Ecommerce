from django.urls import path
from .views import create_purchase,select_shipping_address,set_payment_method_view,select_billing_profile

urlpatterns = [
    
    path('',create_purchase,name='create_purchase'),
    path('set_shipping_addr',select_shipping_address,name='select_shipping_address'),
    path('set_payment_method',set_payment_method_view, name='set_payment_method'),
    path('select_billing_profile',select_billing_profile, name='select_billing_profile'),

]