from django.shortcuts import render,redirect,HttpResponse
from django.http import JsonResponse
from cart.models import Cart,cart_item
from shipping_profile.models import Shipping_Profile
from billing_profile.models import Card, Billing_Profile,Payments
from purchase.models import Purchase
from .models import Orders,order_item
from accounts.models import Profile
from products.models import Product
import stripe
from django.conf import settings
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
stripe.api_key = 'sk_test_8FspIcfPQB72KzJnfwXM2GXj00G7rH0TK5'
# Create ysour views here.
def order_home(request):
    if request.user.is_authenticated:
        try:
            purchase = Purchase.objects.get(user=request.user)
            cart =   Cart.objects.get(id=purchase.cart_id)
            shipping = Shipping_Profile.objects.get(id=purchase.shipping_profile)
            billing  = Billing_Profile.objects.get(id=purchase.billing_profile)

            if purchase.card != -1:
                card = Card.objects.get(id=purchase.card)
            else:
                card = 'COD'
                
            context = {'cart':cart, 'shipping':shipping,'payment':card,'billing':billing}
            return render(request,'order_home.html',context=context)
        except Purchase.DoesNotExist:
            return redirect('/cart')
        return redirect('/')
    
def place_order(request):
    if request.user.is_authenticated:
        try:
            purchase = Purchase.objects.get(user=request.user) 
            profile  = Profile.objects.get(user=request.user)
            cart     = Cart.objects.get(id=purchase.cart_id)
            shipping  = Shipping_Profile.objects.get(id=purchase.shipping_profile)
            billing   = Billing_Profile.objects.get(id=purchase.billing_profile)
            items =     cart.cart_item.all()
            in_stock  = True
            for item in items:
                 product_obj=Product.objects.get(id=item.product.id)
                 if product_obj.stock < item.quantity:
                     in_stock = False
                     break
            if in_stock == False:
                return JsonResponse({'Error':True,'Message':'Opps! Some of the items are out of stock, Please Remove them or reduce the quantity and Try Again!'})
                

            order_obj =  Orders.objects.create(user=request.user,order_status='ordered',total=cart.total, shipping_proile=shipping, billing_profile=billing)

            for item in items:
                order_item_obj = order_item.objects.create(product=item.product, quantity=item.quantity, total=item.total)
                order_obj.order_item.add(order_item_obj)
                product_obj=Product.objects.get(id=item.product.id)
                product_obj.stock=product_obj.stock-item.quantity
                product_obj.save()
            order_obj.save()
            

            if purchase.card==-1:
                payment = Payments.objects.create(order_id=order_obj.order_id,amount=order_obj.total,payement_method='COD')
            else:
                cid=Card.objects.get(id=purchase.card).stripe_id
                c=stripe.Charge.create(
                    amount = int(order_obj.total),
                    currency="inr",
                    card   = cid,
                    customer=request.user.stripe_id,
                    description="Charge for order: "+ order_obj.order_id,
                )
                Payments.objects.create(order_id=order_obj.order_id,amount=order_obj.total,payement_method=c.payment_method,paid=c.paid,stripe_id=c.id)

                print(request.user.email)
            
                
            for item in items:
                i = cart_item.objects.get(id=item.id)
                i.delete()
            cart.delete()
            purchase.delete()
            message = Mail(from_email=settings.EMAIL_HOST_USER,to_emails=request.user.email,)
            message.template_id ='d-ff29f5ad904541d28a78b22c7946784f'
            message.dynamic_template_data = {'name' : profile.Name , 'order':order_obj.order_id, 'time':order_obj.created.strftime('%d-%m-%Y'), 'Fname':shipping.First_Name,'Lname':shipping.Last_Name, 'Address':shipping.Address.Address, 'phone':shipping.Phone,'payment':str(order_obj.total)}
            SendGridAPIClient(settings.SENDGRID_KEY).send(message)
            return JsonResponse({"Message":"Your Order has been placed successfully. Thanks for ordering.",'Success':True})
        except Purchase.DoesNotExist:
            return redirect("/")
    return redirect("/")

def my_orders(request):
    if request.user.is_authenticated:
        orders = Orders.objects.filter(user=request.user)
        profile = Profile.objects.get(user=request.user)
        return render(request,'my_orders.html',context={'orders':orders,'profile':profile})
    return redirect("/")

