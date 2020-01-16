from django.shortcuts import render, get_object_or_404
from django.http import  HttpResponse
from accounts.models import Profile
def Home(request):
    context={}
    if request.user.is_authenticated:
        profile = Profile.objects.get(user=request.user)
        context={'profile':profile}


    return render(request,'Home.html',context=context)