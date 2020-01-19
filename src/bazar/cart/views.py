from django.shortcuts import render,HttpResponse,redirect
from django.http import HttpResponseRedirect,JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Cart,cart_item
from  products.models import Product
from django.urls import reverse
from analytics.models import ObjectViewed
from accounts.models import Profile
from analytics.utils import get_client_ip
from django.db.models import Q

# Create your views here.

@login_required
def cart_home(request):
    if request.user.is_authenticated:
        
        try:
            profile = Profile.objects.get(user=request.user)
            qs = Cart.objects.get(user=request.user)
            
            return render(request,"cart_home.html",context={'cart':qs,'profile':profile})
        except Cart.DoesNotExist:    
            return render(request,"cart_home.html",context={'cart':None,'profile':profile})

    return HttpResponse("Login first")


def cart_add(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            pid=request.POST.get('product')
            q  = request.POST.get('q')
            print(q)
            try:
                product =   Product.objects.get(id=pid)
                cart_obj =  Cart.objects.get(user=request.user)
                Cart_item = cart_obj.cart_item.filter(product=product)
                if Cart_item.exists():
                    item = Cart_item.first()
                    item.quantity = item.quantity + int(q)
                    item.save()
                else:
                    item = cart_item.objects.create(product=product,quantity=q)
                    cart_obj.cart_item.add(item)

                cart_obj.save()
                return JsonResponse({"Message":'Product has been added to your cart successfully'})
        
            except Cart.DoesNotExist:   
                cart_obj=Cart.objects.create(user=request.user)
                item = cart_item.objects.create(product=product,quantity=q)
                cart_obj.cart_item.add(item)
                cart_obj.save()

                return JsonResponse({"Message":'Product has been added to your cart successfully'})
            except Product.DoesNotExist:
                return JsonResponse({"Message":'Opps: Something Went Wrong!'})
        else:
            return JsonResponse({"Message":'Opps: Something Went Wrong!'})
    return redirect("/")

def cart_remove(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            pid=request.POST.get('product')
            try:
                product =   Product.objects.get(id=pid)
                cart_obj =  Cart.objects.get(user=request.user)
                Cart_item = cart_obj.cart_item.filter(product=product).delete()
                cart_obj.save()
                items = cart_obj.cart_item.all()
                if not items.exists():
                    cart_obj.delete()
                messages.success(request,"Item Has been Removed Successfully")
                
                return redirect("/cart")
        
            except Product.DoesNotExist:
                return HttpResponse('<!DOCTYPE html> <html>    <head>       <title>Page Not Found </title>       <meta http-equiv = "refresh" content = "2; url = /products/product_list/" />    </head>    <body> <h1> Error 404!</h1>   <h2>Page Not Found</h2>   </body> </html>')
        else:
            return HttpResponse('<!DOCTYPE html> <html>    <head>       <title>Error </title>       <meta http-equiv = "refresh" content = "2; url = /" />    </head>    <body> <h1> Error 404!</h1>   <h2>Not a valid request</h2>   </body> </html>')
    return redirect("/")