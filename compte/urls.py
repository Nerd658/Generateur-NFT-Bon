from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('connexion/', views.connexion , name="connexion"),
    path('inscription/', views.inscription , name="inscription")
]
