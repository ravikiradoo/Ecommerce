from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .models import User
from django.http import JsonResponse

# Create your views here.

def loginpage(request):
    return render(request,'login.html')

def register(request):
    email = request.POST.get("email")
    password=request.POST.get("password")
    user = User.objects.filter(email=email)
    if user.exists():
        return JsonResponse({"Message":"Email Id is Already Taken"})
    user=User.objects.create_user(email=email,password=password)
    if User:
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

