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

    num1=request.GET["num1"]
    num2=request.GET["num2"]
    if  num1 is not '' and num2 is not '':
     try :
       res=int (num1)+int(num2)
       return render(request,'ADD.html',{'res':res})
     except ValueError:
        return HttpResponse("<h1>plz enter Valid Number!!!!!!!!!</h1>")
    else:
        return HttpResponse("<h1>plz enter Number</h1>")
def sub(request):
    num1 = request.GET["num1"]
    num2 = request.GET["num2"]
    if num1 is not '' and num2 is not '':
       try :
        res =int( num1) -int (num2)
        return render(request,'Sub.html',{'RES':res})
       except ValueError:
           return  HttpResponse("<h1>Invalid Input</h1>")

    else :
        return HttpResponse("<h1>plz enter Number</h1>")

def LOGIN(request) :

    num1=request.POST["num1"]
    num2=request.POST["num2"]
    if  num1 is not '' and num2 is not '':
     try :
       res=int (num1)+int(num2)
       return render(request,'ADD.html',{'res':res})
     except ValueError:
        return HttpResponse("<h1>plz enter Valid Number!!!!!!!!!</h1>")
    else:
        return HttpResponse("<h1>plz enter Number</h1>")