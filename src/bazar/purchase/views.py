from django.shortcuts import render,redirect,HttpResponse
from .models import Purchase
# Create your views here.
def create_purchase(request):
    if request.user.is_authenticated:
        cid= request.POST.get("cid")
        try:
            ps= Purchase.objects.get(user=request.user)
            ps.delete()
            Purchase.objects.create(user=request.user,cart_id=cid)
        except Purchase.DoesNotExist:
            Purchase.objects.create(user=request.user,cart_id=cid)
    return redirect("/shipping/Shipping_Profiles")

def select_shipping_address(request):
    if request.user.is_authenticated:
        try:
             ps= Purchase.objects.get(user=request.user)
             ps.shipping_profile=request.POST.get("profile")
             ps.save()
             return redirect("/billing/get_billing_profile")
        except Purchase.DoesNotExist:
            return redirect("/")

def select_billing_profile(request):
    if request.user.is_authenticated:
        try:
             ps= Purchase.objects.get(user=request.user)
             ps.billing_profile=request.POST.get("profile")
             ps.save()
             return redirect("/billing/select_payment_method")
        except Purchase.DoesNotExist:
            return redirect("/")


def set_payment_method_view(request):
    if request.user.is_authenticated:
        try:
             ps= Purchase.objects.get(user=request.user)
             print(request.POST)
             ps.card = request.POST.get("pmethod")
             ps.save()
             return redirect("/order")
        except Purchase.DoesNotExist:
            return redirect("/")
