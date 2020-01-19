from django.urls import path,reverse_lazy
from .views import loginpage,signin,signout,register,email_verification,account_home,security,change_password_page,change_password_view,change_profile
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('login/',loginpage,name='loginpage'),
    path('change_password_page/',change_password_page,name='changepassword'),
    path('change_password/',change_password_view,name='change_password'),
    path('change_profile/',change_profile,name='change_profile'),
    path('register',register,name='register'),
    path('signin',signin,name='login'),
    path('signout',signout,name='logout'),
    path('verification/<str:key>/',email_verification,name='email_verification'),
    path('home/',account_home,name='account_home'),
    path('security',security,name='security')

]