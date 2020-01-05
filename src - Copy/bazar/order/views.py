from django.shortcuts import render,redirect,HttpResponse
from cart.models import Cart,cart_item
from shipping_profile.models import Shipping_Profile
from billing_profile.models import Card, Billing_Profile,Payments
from purchase.models import Purchase
from .models import Orders,order_item
import stripe
stripe.api_key = 'sk_test_8FspIcfPQB72KzJnfwXM2GXj00G7rH0TK5'
# Create ysour views here.
def order_home(request):
    if request.user.is_authenticated:
        try:
            purchase = Purchase.objects.get(user=request.user)
            cart =   Cart.objects.get(id=purchase.cart_id)
            shipping = Shipping_Profile.objects.get(id=purchase.shipping_profile)

            if purchase.card != -1:
                card = Card.objects.get(id=purchase.card)
            else:
                card = 'COD'
                
            context = {'cart':cart, 'shipping':shipping,'payment':card}
            return render(request,'order_home.html',context=context)
        except Purchase.DoesNotExist:
            return redirect('/cart')
        return redirect('/')
    
def place_order(request):
    if request.user.is_authenticated:
        try:
            purchase = Purchase.objects.get(user=request.user) 
            cart     = Cart.objects.get(id=purchase.cart_id)
            shipping  = Shipping_Profile.objects.get(id=purchase.shipping_profile)
            billing   = Billing_Profile.objects.get(user=request.user)
            items =     cart.cart_item.all()
            order_obj =  Orders.objects.create(user=request.user,order_status='ordered',total=cart.total, shipping_proile=shipping, billing_profile=billing)

            for item in items:
                order_item_obj = order_item.objects.create(product=item.product, quantity=item.quantity, total=item.total)
                order_obj.order_item.add(order_item_obj)
            order_obj.save()
            if purchase.card==-1:
                payment = Payments.objects.create(order_id=order_obj.order_id,amount=order_obj.total,payement_method='COD')
            else:
                cid=Card.objects.get(id=purchase.card).stripe_id
                c=stripe.Charge.create(
                    amount = int(order_obj.total),
                    currency="inr",
                    card   = cid,
                    customer=billing.stripe_id,
                    description="Charge for order: "+ order_obj.order_id,
                )
                Payments.objects.create(order_id=order_obj.order_id,amount=order_obj.total,payement_method=c.payment_method,paid=c.paid,stripe_id=c.id)
                print(c)
            
                
            for item in items:
                i = cart_item.objects.get(id=item.id)
                i.delete()
            cart.delete()
            purchase.delete()
            return HttpResponse('<!DOCTYPE html> <html>    <head>       <title>Order Placed </title>       <meta http-equiv = "refresh" content = "2; url = /order/my-orders" />    </head>    <body>    <h1>  Thanks For Ordering </h1>   </body> </html>')
        except Purchase.DoesNotExist:
            return redirect("/")
    return redirect("/")

def my_orders(request):
    if request.user.is_authenticated:
        orders = Orders.objects.filter(user=request.user)
        return render(request,'my_orders.html',context={'orders':orders})
    return redirect("/")