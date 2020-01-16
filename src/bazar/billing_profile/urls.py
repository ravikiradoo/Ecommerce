from django.urls import path
from .views import payment_method_view,create_payment_method_view,select_payment_method_view,Get_Billing_Profiles,Add_Billing_Profile

urlpatterns = [
     path('payment_method',payment_method_view, name='payment_method'),
      path('create_payment_method',create_payment_method_view, name='create_payment_method'),
      path('select_payment_method',select_payment_method_view, name='select_payment_method'),
      path('get_billing_profile',Get_Billing_Profiles, name='get_billing_profile'),
      path('add_billing_profile',Add_Billing_Profile, name='add_billing_profile'),
]

