from django.shortcuts import render,redirect
from .models import *
from .forms import*
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib import sessions

def index(request):
    form=UserForm()
    return render(request,'index.html',{"form":form})





def formsave(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        pwd=request.POST['pwd']
        if User.objects.filter(email=email).exists():
            form=UserForm()
            messages.error(request,"email already exists try with new email")
            return render(request,'index.html',{"form":form,"error":"Email Already Exists"})
        else:
            user=User.objects.create(name=name,email=email,pwd=pwd)
            user.save()
            name=User.objects.get(email=email)
            request.sessions["email"]=email
            messages.success(request,"successfully registered")
            return render(request,'index.html',{"name":name})
            





def contact(request):
    form=UserForm()
    return render(request,'contact.html',{"form":form})




def games(request):
    g=Game.objects.all()
    form=UserForm()
    return render(request,'review.html',{'g':g,"form":form})



def gameview(request,id):
    g=Game.objects.filter(id=id)
    form=UserForm()
    return render(request,'gameview.html',{'g':g,"form":form})