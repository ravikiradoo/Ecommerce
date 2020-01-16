from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .models import User,Profile
from django.http import JsonResponse
from django.core.mail import send_mail
from django.conf import settings
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

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
        return JsonResponse({"Message":"Email Id is Already Taken"})
    user=User.objects.create_user(email=email,password=password)
    if User:
        profile = Profile.objects.create(user=user,Name=name, phone=mobile)
        message = Mail(from_email=settings.EMAIL_HOST_USER,to_emails=email,)
        message.template_id ='d-222f7a5ffe9446409a43c7d0c16feb4b'
        message.dynamic_template_data = {'name' : name}
        SendGridAPIClient(settings.SENDGRID_KEY).send(message)
        return JsonResponse({"Message":"Account has been created successfully Please Verify your Email Id"})
    else:
        return JsonResponse({"Message":"Something Went Wrong Please Try Again"})
    
    


    

def signin(request):
    email=request.POST.get("email")
    password=request.POST.get("password")
    user = authenticate(request,email=email,password=password)
    print(user)
    if user:
        login(request,user)
        return redirect("/")
    else:
        message = "Invalid User Name or Password"
        return render(request, "login.html", {'error':message})

def signout(request):
    logout(request)
    return redirect("/")

