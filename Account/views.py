from django.shortcuts import render,redirect
from django.contrib.auth.models import  User,auth
from django.contrib import messages
from django.http import HttpResponse
# Create your views here.
def register(request) :
    #sice in reg.html the action ="" is not defined to any other page like pervious to add or sub
    #We will use this same /register based on method ,  GET OR POST
    if request.method =='POST':
     firstname=request.POST['first_name']
     lastname = request.POST['last_name']
     username = request.POST['username']
     email = request.POST['emailid']
     password = request.POST['password']
     password_cnf = request.POST['password_cnf']
     if password ==password_cnf :
         if User.objects.filter(username=username).exists() :
              messages.info(request,"USER NAME TAKEN PLZ ENTER OTHER ")
              return  redirect('/accounts/register')
         elif User.objects.filter(email=email).exists() :
             messages.info(request, "EMAIL  TAKEN PLZ ENTER OTHER ")
             return redirect('/accounts/register')
         else :
               user=User.objects.create_user(username=username,password=password_cnf,email=email,first_name=firstname,last_name=lastname)
               user.save()
         return  redirect('/travell')
     else  :
         return HttpResponse("INVALID PASSWORD")

    if request.method =='GET' :

       return  render(request,'reg.html')