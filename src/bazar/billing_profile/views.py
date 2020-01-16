from django.shortcuts import render,redirect,HttpResponse
from django.http import JsonResponse
from .models import Billing_Profile,Card
from addresses.models import Address
from accounts.models import User
from .forms import PaymentForm
import stripe
from django import forms
from accounts.models import User
stripe.api_key = 'sk_test_8FspIcfPQB72KzJnfwXM2GXj00G7rH0TK5'
# Create your views here.


def Get_Billing_Profiles(request):
    if  request.user.is_authenticated:
        profiles=Billing_Profile.objects.filter(user=request.user)
        return render(request,'add_billing_profile.html',context={'profiles':profiles})
    else:
        return redirect('/')

def Add_Billing_Profile(request):
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
            profile   = Billing_Profile.objects.create(user=request.user,First_Name=First_Name,Last_Name=Last_Name,Phone=Phone,Address=address)
            response =  {'Profile_id':profile.id}
            return    JsonResponse(response)
        else:
            return redirect('/')
    else:
        return redirect('/')
        


def select_payment_method_view(request):
    if request.user.is_authenticated:
        cards  = Card.objects.filter(user=request.user)
        PaymentForm.base_fields['id'] = forms.ModelChoiceField(queryset=cards,widget=forms.RadioSelect,empty_label=None)
        form = PaymentForm()
        return render(request,'payment_method.html',{'cards':cards})

STRIPE_PUB_KEY = 'pk_test_u0qds0S6OkUjKyiJ3CfKfjVp00GCoGJjgc'

def payment_method_view(request):
    
    return render(request,'payment_method.html', {"pub_key":STRIPE_PUB_KEY})


def create_payment_method_view(request):
    if request.user.is_authenticated:
        if  request.method=='POST' and request.is_ajax():
            user      = User.objects.get(id= request.user.id)
            cid       = user.stripe_id
            token     = request.POST.get("stripeToken")
            customer   = stripe.Customer.retrieve(cid)
            response   = customer.sources.create(source=token)
            if response:
                stripe_id = response.id
                month     = response.exp_month
                year      = response.exp_year
                brand     = response.brand
                last4     = response.last4
                card   = Card.objects.create(user=user,stripe_id=stripe_id,Month=month,Year=year,brand=brand,last4=last4)
                return JsonResponse({"message":"Card Added successfully","card":card.id})
            else:
                return JsonResponse({"success":False, "error":"Something Went Wrong"})
        return redirect("/")
    return redirect("/")

    
