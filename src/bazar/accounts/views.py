from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import authenticate,login,logout
from .models import User,Profile
from django.http import JsonResponse
from django.core.mail import send_mail
from django.conf import settings
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from django.contrib  import messages
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm

# Create your views here.

def loginpage(request):
    return render(request,'login.html')

def register(request):
    email = request.POST.get("email")
    password=request.POST.get("password")
    name=request.POST.get("name")
    mobile=request.POST.get('mobile')
    
    user = User.objects.filter(email=email)
    if user.exists():
        return JsonResponse({"Message":"Email Id is Already Taken","Error":True})
    user=User.objects.create_user(email=email,password=password)
    if User:
        profile = Profile.objects.create(user=user,Name=name, phone=mobile)
        message = Mail(from_email=settings.EMAIL_HOST_USER,to_emails=email,)
        message.template_id ='d-222f7a5ffe9446409a43c7d0c16feb4b'
        link='http://127.0.0.1:8000/accounts/verification/'+user.key
        message.dynamic_template_data = {'name' : name,'link':link ,'Email':user.email }
        SendGridAPIClient(settings.SENDGRID_KEY).send(message)
        return JsonResponse({"Message":"Account has been created successfully Please Verify your Email Id", 'Success':True})
    else:
        return JsonResponse({"Message":"Something Went Wrong Please Try Again"})
    
    
def account_home(request):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user=request.user)
        return render(request,'account_home.html',context={'profile':profile})
    return render("/")

    

def signin(request):
    email=request.POST.get("email")
    password=request.POST.get("password")
    user = authenticate(request,email=email,password=password)
    print(user)
    if user:
        if not user.is_active:
            messages.error(request,"Your Account is Blocked. Please Contact Our Customer Care")
            return redirect("/accounts/login")

        if not user.is_email_confirmed:
            messages.error(request,"Your Email has not been verified yet. Please Verify")
            return redirect("/accounts/login")

        login(request,user)
        return redirect("/")
    else:
        messages.error(request,"Invalid User Name or Password")
        return redirect("/accounts/login")
def signout(request):
    logout(request)
    return redirect("/")

def email_verification(request,key=None):
    try:
        user = User.objects.get(key=key)
        if not user.confirm_email:
            user.confirm_email = True
            user.save()
            return redirect("/accounts/login")
        else:
            messages.info(request,"Email Id Is Already Verified. Please Login")
            return redirect("/accounts/login")

    except User.DoesNotExist:
        return HttpResponse("Not a Valid Link")

def security(request):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user=request.user)
        return render(request,'security.html',context={'profile':profile})
    else:
        return redirect("/accounts/login")

def change_password_page(request):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user=request.user)
        return render(request,'change_password.html',context={'profile':profile})
    else:
        return redirect("/")

def change_password_view(request):
    if request.user.is_authenticated:
        old_password=request.POST.get('old_password')
        password1 = request.POST.get('new_password1')
        password2 = request.POST.get('new_password2')
        print(old_password)
        user = authenticate(email=request.user.email,password=old_password)
        if not user:
            messages.error(request,"Please Enter Correct Old Password")
            return redirect("/accounts/change_password_page")
        if password1 != password2:
            messages.error(request,"Password did not match ")
            return redirect("/accounts/change_password_page")


        form = PasswordChangeForm(user=request.user,data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Password Changed Successfully. Please Login Again With New Password')
            return redirect("/accounts/login")
        else:
            messages.error(request,"Something Went Wrong")
            return redirect("/accounts/change_password_page")

    else:
        return redirect("/accounts/login")

    
def change_profile(request):
    if request.user.is_authenticated:
        name = request.POST.get("name")
        phone = request.POST.get("mobile")
        profile = Profile.objects.get(user=request.user)
        profile.Name = name
        profile.phone = phone
        profile.save()
        messages.success(request,"Profile Changed Successfully")
        return redirect("/accounts/security")
    return  redirect("/accounts/login")




        



    

