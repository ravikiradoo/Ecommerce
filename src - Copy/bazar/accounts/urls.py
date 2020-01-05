from django.urls import path
from .views import loginpage,signin,signout
urlpatterns = [
    path('login',loginpage,name='loginpage'),
    path('signin',signin,name='login'),
    path('signout',signout,name='logout')
]