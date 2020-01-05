from django.urls import path
from .views import Get_Shipping_Profiles,Add_Shipping_Profile

urlpatterns = [
    path('Shipping_Profiles/',Get_Shipping_Profiles, name='get_shipping_profiles'),
     path('Add_Profile/',Add_Shipping_Profile, name='add_shipping_profile'),
]