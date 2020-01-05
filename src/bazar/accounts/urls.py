from django.urls import path
from .views import loginpage,signin,signout,register
urlpatterns = [
    path('login',loginpage,name='loginpage'),
     path('register',register,name='register'),
    path('signin',signin,name='login'),
    path('signout',signout,name='logout')
]