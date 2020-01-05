from django.shortcuts import render, get_object_or_404
from django.http import  HttpResponse

def Home(request):
    return render(request,'Home.html',context={})