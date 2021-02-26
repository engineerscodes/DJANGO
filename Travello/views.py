from django.shortcuts import render
from django.http import  HttpResponse
# Create your views here.
from .models import Desinations

def index(request):
    dests=Desinations.objects.all()
    return  render(request,'index.html',{'dests':dests})

