from django.shortcuts import render,redirect
from django.http import  HttpResponse
# Create your views here.
from .models import Desinations



def index(request):
    if request.user.is_authenticated:
      dests=Desinations.objects.all()
      return  render(request,'index.html',{'dests':dests})
    else :
        return redirect('accounts/login')


