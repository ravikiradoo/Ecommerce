from django.urls import path
from .views import order_home,place_order,my_orders

urlpatterns = [
    
    path('',order_home,name='order'),
    path('place/',place_order,name='place_order'),
    path('my-orders/',my_orders,name='my_orders'),

]
