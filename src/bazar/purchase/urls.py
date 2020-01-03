from django.urls import path
from .views import create_purchase,select_shipping_address,set_payment_method_view

urlpatterns = [
    
    path('',create_purchase,name='create_purchase'),
    path('set_shipping_addr',select_shipping_address,name='select_shipping_address'),
    path('set_payment_method',set_payment_method_view, name='set_payment_method'),

]