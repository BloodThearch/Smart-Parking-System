from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.checkout, name="checkout"),
    path('checkOutComp', views.checkoutComp, name="checkoutComp")
]