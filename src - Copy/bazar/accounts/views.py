from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
# Create your views here.

def loginpage(request):
    return render(request,'login.html')

def signin(request):
    username=request.POST.get("username")
    password=request.POST.get("password")
    print(username)
    print(password)
    user = authenticate(request,username=username,password=password)
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

