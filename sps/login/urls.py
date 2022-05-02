from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.loginPage, name="loginPage"),
    path('wrongPassword', views.wrongpwd, name="wrongpwd"),
    path('unregisteredNo', views.unregisteredNumber, name="unregisteredNumber"),
]