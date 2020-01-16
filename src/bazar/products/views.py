from django.shortcuts import render, get_object_or_404
from django.http import  HttpResponse,HttpResponseRedirect
from .models import Product
from django.db.models import Q
from analytics.signals import object_viewed_signal
from accounts.models import Profile

# Create your views here.

def product_list(request,category=None):
    query  = request.GET.get('q',None)
    print(request.GET)
    print(query)
    profile=Profile.objects.get(user=request.user)
    context={'profile':profile}
    
    if not query and not category:
        return HttpResponseRedirect("/")
    if category:
        qs = Product.objects.filter(category=category)
        context = {
    'products' : qs,
    'profile':profile
    }
        return render(request,"products.html",context=context)

    q = ( Q(title__icontains=query) | Q(description__icontains=query)| Q(tag__tag__icontains=query))
    qs = Product.objects.filter(q).distinct()
    context = {
    'products' : qs,
    'profile':profile
    }
    return render(request,"products.html",context)
        
def product_detail(request,id=None):
    context = {}
    try:
        product = Product.objects.get(pk=id)
        profile=Profile.objects.get(user=request.user)
        context = {'product':product,'profile':profile}
        object_viewed_signal.send(product.__class__,instance=product,request=request)
    except Product.DoesNotExist:
        return HttpResponse('<!DOCTYPE html> <html>    <head>       <title>Page Not Found </title>       <meta http-equiv = "refresh" content = "2; url = /products/product_list/" />    </head>    <body> <h1> Error 404!</h1>   <h2>Page Not Found</h2>   </body> </html>')
    return render(request,'detail.html',context)