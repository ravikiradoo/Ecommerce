"""bazar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import Home
from products.views import product_list
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home),
    path('search/',product_list,name='search_product'),
    path('products/',include(('products.urls','products'),namespace='products')),
    path('cart/',include(('cart.urls','cart'),namespace='cart')),
    path('order/',include(('order.urls','order'),namespace='order')),
    path('shipping/',include(('shipping_profile.urls','shipping_profile'),namespace='shipping_profile')),
    path('billing/',include(('billing_profile.urls','billing_profile'),namespace='billing_profile')),
    path('purchase/',include(('purchase.urls','purchase'),namespace='purchase')),
    path('accounts/',include(('accounts.urls','account'),namespace='account')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)