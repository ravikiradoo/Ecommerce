from django.urls import path
from .views import Get_Shipping_Profiles,Add_Shipping_Profile,Show_Shipping_Profiles,add_new_profile,edit_profile,delete_profile

urlpatterns = [
    path('Shipping_Profiles/',Get_Shipping_Profiles, name='get_shipping_profiles'),
     path('Add_Profile/',Add_Shipping_Profile, name='add_shipping_profile'),
     path('Show_Shipping_Profiles/',Show_Shipping_Profiles, name='show_shipping_profile'),
     path('add_new_profile/',add_new_profile, name='add_new_profile'),
     path('edit_profile/',edit_profile, name='edit_profile'),
     path('delete/',delete_profile, name='delete_profile'),
]
