
from django.urls import path

from . import  views

urlpatterns = [
    path('', views.home,name="HOME"),
    path('Learn/',views.LEAN,name="LEARN"),
    path('add',views.add,name="add")
]
