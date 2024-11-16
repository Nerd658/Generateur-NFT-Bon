from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.acceuil , name="acceuil"),
    path('contact', views.contact , name="contact"),
    path('connexion', views.connexion , name="connexion"),
    path('deconnexion', auth_views.LogoutView.as_view(next_page='acceuil'), name="deconnexion"),
    path('form', views.mint , name="mint"),
    path('Validation', views.validate_voucher , name="validation"),
    
    
]