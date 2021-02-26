
from django.urls import path

from . import  views

urlpatterns = [
    path('', views.home,name="HOME"),
    path('Learn/',views.LEAN,name="LEARN"),
    path('add',views.add,name="add"),
    path('sub',views.sub,name="SUB"),
    path('LOGIN',views.LOGIN,name="Login")
]
