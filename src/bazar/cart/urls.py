from django.urls import path
from .views import cart_home,cart_add,cart_remove

urlpatterns = [
path('',cart_home),
path('add/',cart_add,name='add'),
path('remove/',cart_remove,name='remove')

]