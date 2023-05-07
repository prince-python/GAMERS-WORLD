from django.shortcuts import render
from .models import *



def index(request):
    
    return render(request,'index.html')






def contact(request):
    return render(request,'contact.html')




def games(request):
    g=Game.objects.all()
    return render(request,'review.html',{'g':g})



def gameview(request,id):
    g=Game.objects.filter(id=id)
    return render(request,'gameview.html',{'g':g})