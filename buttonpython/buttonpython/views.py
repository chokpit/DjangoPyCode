from django.shortcuts import render
from .scripto import *





def button(request):
    return render(request,'home.html')

def output(request):
    #data = requests.get("https://www.ynet.co.il") #good line
    #print(data.text) #this line is not working anyways
    #data=data.text #good line
    return render(request,'home.html',{'data':func1()})
    #return render(request,'home.html',{'data':data})
