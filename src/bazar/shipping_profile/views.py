from django.shortcuts import render,redirect
from .models import Shipping_Profile
from addresses.models import Address
from django.http import JsonResponse
from accounts.models import Profile
from django.contrib import messages
# Create your views here.

def Get_Shipping_Profiles(request):
    if  request.user.is_authenticated:
        profiles=Shipping_Profile.objects.filter(user=request.user)
        cart_id=request.POST.get("cart")
        return render(request,'Delivery_Address.html',context={'profiles':profiles, 'cart':cart_id})
    else:
        return redirect('/')


def Show_Shipping_Profiles(request):
    if  request.user.is_authenticated:
        profiles=Shipping_Profile.objects.filter(user=request.user)
        profile=Profile.objects.get(user=request.user)
        cart_id=request.POST.get("cart")
        return render(request,'shipping_profiles.html',context={'profiles':profiles,'profile':profile} )
    else:
        return redirect('/')

def add_new_profile(request):
    if request.user.is_authenticated:
        if request.method == "GET":
            return render(request,"add_profile.html")
        if request.method == "POST":
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
            messages.success(request,"Address Added Successfully")
            return redirect("/shipping/Show_Shipping_Profiles/")
    else:
        return redirect("/accounts/login/")

def edit_profile(request):
    if request.user.is_authenticated:
        if request.method == "GET":
            pid = request.GET.get("pid")
            sprofile = Shipping_Profile.objects.get(id=pid)
            return render(request,"edit_profile.html",context={'sprofile':sprofile})
        if request.method == "POST":
                pid = request.POST.get("pid")
                profile = Shipping_Profile.objects.get(id=pid)
                address = profile.Address
                profile.First_Name=request.POST.get('First_Name')
                profile.Last_Name = request.POST.get('Last_Name')
                profile.Phone     = request.POST.get('Phone')
                address.Address  = request.POST.get('Address')
                address.City      = request.POST.get('City')
                address.State     = request.POST.get('State')
                address.Country   = request.POST.get('Country')
                address.zipcode   = request.POST.get('Zipcode')
                address.save()
                profile.Address = address
                profile.save()
                messages.success(request,"Address Changed Successfully")
                return redirect("/shipping/Show_Shipping_Profiles/")
    else:
        return redirect('/')

def delete_profile(request):
    if request.user.is_authenticated:
        pid = request.POST.get("pid")
        profile = Shipping_Profile.objects.get(id=pid)
        profile.delete()
        messages.success(request,"Address Deleted Successfully")
        return redirect("/shipping/Show_Shipping_Profiles/")
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
        