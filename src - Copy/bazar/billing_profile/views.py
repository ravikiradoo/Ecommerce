from django.shortcuts import render,redirect,HttpResponse
from django.http import JsonResponse
from .models import Billing_Profile,Card
from .forms import PaymentForm
import stripe
from django import forms
stripe.api_key = 'sk_test_8FspIcfPQB72KzJnfwXM2GXj00G7rH0TK5'
# Create your views here.

def select_payment_method_view(request):
    if request.user.is_authenticated:
        try:
            bp = Billing_Profile.objects.get(user=request.user)
            cards  = bp.card_set.filter()
            PaymentForm.base_fields['id'] = forms.ModelChoiceField(queryset=cards,widget=forms.RadioSelect,empty_label=None)
            form = PaymentForm()
            return render(request,'payment_method.html',{'cards':cards})
        except bp.DoesNotExist:
            return redirect("/")
    return redirect("/")
STRIPE_PUB_KEY = 'pk_test_u0qds0S6OkUjKyiJ3CfKfjVp00GCoGJjgc'

def payment_method_view(request):
    
    return render(request,'payment_method.html', {"pub_key":STRIPE_PUB_KEY})


def create_payment_method_view(request):
    if request.user.is_authenticated:
        if  request.method=='POST' and request.is_ajax():
            b_profile = Billing_Profile.objects.get(user=request.user)
            cid       = b_profile.stripe_id
            token     = request.POST.get("stripeToken")
            customer   = stripe.Customer.retrieve(cid)
            response   = customer.sources.create(source=token)
            if response:
                stripe_id = response.id
                month     = response.exp_month
                year      = response.exp_year
                brand     = response.brand
                last4     = response.last4
                card   = Card.objects.create(Billing_Profile=b_profile,stripe_id=stripe_id,Month=month,Year=year,brand=brand,last4=last4)
                return JsonResponse({"message":"Card Added successfully","card":card.id})
            else:
                return HttpResponse("Something went wrong",status_code=401)
        return redirect("/")
    return redirect("/")

    
