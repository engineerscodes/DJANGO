from django.shortcuts import render
from django.http import  HttpResponse

# Create your views here.

def home(request):
     #return HttpResponse("<h1> NAVEEN C</h1>")
     #return  render(request,'home.html')
     return render(request, 'home.html',{'name':'NAVEEN TECH'})


def LEAN(request) :
     return HttpResponse("<b><i>LEARN WITH ME !!!!!!!@</i></b>")

def add (request):

    num1=int(request.GET["num1"])
    num2=int(request.GET["num2"])
    res=num1+num2
    return render(request,'ADD.html',{'res':res})