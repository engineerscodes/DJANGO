

from django.urls import path,include
from . import views

urlpatterns = [
    path("register",views.register,name="REG"),
    path("login",views.Login,name="LOGINS"),
    path("logout",views.Logout,name="LOGOUT")

]