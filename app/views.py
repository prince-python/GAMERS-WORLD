from django.shortcuts import render,redirect
from .models import *
from .forms import*
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib import sessions
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail



def index(request):
    form=UserForm()
    return render(request,'index.html',{"form":form})





def formsave(request):
    try:
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
                messages.success(request,"successfully registered")
                return render(request,'index.html',{"name":name})
    except:
        print("error data")
                


def login(request):
    try:
        if request.method =='POST':
                email=request.POST['email']
                pwd=request.POST['pwd']
                if User.objects.filter(email=email).exists() and User.objects.filter(pwd=pwd).exists():
                    messages.success(request,"LOGIN SUCCESSFULL")
                    form=UserForm()
                    return render(request,'index.html',{"form":form})
                else:
                    messages.error(request,"CHECK EMAIL OR PASSWORD")
                    return render(request,'login.html')
        else:
            return render(request,'login.html')
    except:
        print("cant send ")
        


def contact(request):
    form=UserForm()
    return render(request,'contact.html',{"form":form})


@login_required(login_url="../login/")
def games(request):
    g=Game.objects.all()
    form=UserForm()
    return render(request,'review.html',{'g':g,"form":form})

@login_required(login_url="../login/")
def gameview(request,id):
    g=Game.objects.filter(id=id)
    form=UserForm()
    return render(request,'gameview.html',{'g':g,"form":form})


def send(request):
    try:
        email=request.POST['email']
        msg=request.POST['msg']
        subject=request.POST['subject']
        send_mail(subject,msg,"choudharyprince140@gmail.com",[email])
        form=UserForm()
        return render(request,'contact.html',{"form":form})
    except:
        form=UserForm()
        return render(request,'contact.html',{"form":form})
