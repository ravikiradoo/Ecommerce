from django.shortcuts import render,redirect
from .models import Shipping_Profile
from addresses.models import Address
from django.http import JsonResponse
# Create your views here.

def Get_Shipping_Profiles(request):
    if  request.user.is_authenticated:
        profiles=Shipping_Profile.objects.filter(user=request.user)
        cart_id=request.POST.get("cart")
        return render(request,'Delivery_Address.html',context={'profiles':profiles, 'cart':cart_id})
    else:
        return redirect('/')

def Add_Shipping_Profile(request):
    if request.user.is_authenticated:
        if request.method =='POST':
            First_Name=request.POST.get('First_Name')
            Last_Name = request.POST.get('Last_Name')
            Phone     = request.POST.get('Phone')
            Address_   = request.POST.get('Address')
            City      = request.POST.get('City')
            State     = request.POST.get('State')
            Country   = request.POST.get('Country')
            Zipcode   = request.POST.get('Zipcode')
            address   = Address.objects.create(Address=Address_,City=City,State=State,Country=Country,zipcode=Zipcode)
            profile   = Shipping_Profile.objects.create(user=request.user,First_Name=First_Name,Last_Name=Last_Name,Phone=Phone,Address=address)
            response =  {'Profile_id':profile.id}
            return    JsonResponse(response)
        else:
            return redirect('/')
    else:
        return redirect('/')
        