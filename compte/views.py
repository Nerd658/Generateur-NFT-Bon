from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import re
from django.db.models import Q




def inscription(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        username = request.POST["username"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        
        if User.objects.filter(username=username).exists() :
            messages.error(request, "Un utilisateur avec ce nom existe deja")
        elif len(password1)< 8 :
            messages.error(request, "Le mot de passe doit contenir au moins 8 caractéres")
        elif not re.search(r"\d" , password1) or not re.search(r"[A-Za-z]" , password1) :
            messages.error(request, "Le mot de passe doit etre un melange de chifre et de lettre")
        elif password1!=password2 :
            messages.error(request, "veuillez renseingner les memes mots de passe")
        elif form.is_valid():
            form.save()
            return redirect('connexion')

            
            
            
        
        
    else:
        form = UserCreationForm()
        
    
    return render(request, 'compte/inscription.html', {'form': form})

def connexion(request) :
    
    if request.method == 'POST' :
        
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None :
            login(request , user)
            return redirect('acceuil')
        else:
           messages.error(request, 'Invalid username or password')
    
    return render (request , 'compte/connexion.html')