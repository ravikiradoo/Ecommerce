from django.urls import path
from .views import product_list,product_detail

urlpatterns = [
    path('product_list/', product_list),
    path('product_detail/<int:id>/', product_detail, name='detail'),
    path('<str:category>/', product_list, name='category'),
]

