from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name='home'),
    path("contact", views.contact, name="contact"),
    path("login",views.handeLogin, name="handeLogin"),
    path("logout",views.handelLogout, name="handelLogout"),
    path("checkout",views.checkout, name="checkout"),
    path("items/",views.items, name="items"),
    path("signup",views.handleSignUp, name="handleSignUp"),

]