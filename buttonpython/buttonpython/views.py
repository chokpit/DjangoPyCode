from django.shortcuts import render
from .scripto import *





def button(request):
    return render(request,'home.html')

def output(request):
    return render(request,'home.html',{'data':func1()})