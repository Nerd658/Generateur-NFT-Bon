from django.shortcuts import render
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
from django.contrib.auth.decorators import login_required
# Create your views here.

def acceuil (request) :
    return render(request, 'app/acceuil.html')


def contact (request) :
    return render (request, 'app/contact.html')

def connexion (request) :
    return render (request, 'compte/connexion.html')

# @login_required
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import WalletUser, Transaction , Validation
import json

@csrf_exempt
def mint(request):
    if request.method == 'POST':
        # Récupérer les détails de la transaction sous forme de JSON
        data = json.loads(request.body)
        wallet_address = data.get('walletAddress')
        voucher_id = data.get('voucherId')
        transaction_hash = data.get('transactionHash')

        success = True  # Indicateur de succès
        messages_list = []  # Liste des messages pour les retours

        try:
            # Récupérer ou créer l'utilisateur par son adresse de portefeuille
            user, created = WalletUser.objects.get_or_create(wallet_address=wallet_address)
            
            # Créer la transaction
            transaction = Transaction.objects.create(
                user=user,
                voucher_id=voucher_id,
                transaction_hash=transaction_hash
            )
            messages_list.append(f"Transaction {transaction_hash} pour le bon {voucher_id} ajoutée avec succès.")
        except Exception as e:
            success = False
            messages_list.append(f"Erreur lors de l'ajout de la transaction: {str(e)}")

        # Retourne le message de succès ou d'erreur
        if success:
            return JsonResponse({"success": True, "message": "Transaction enregistrée avec succès!", "details": messages_list}, status=200)
        else:
            return JsonResponse({"success": False, "message": "Erreur lors de l'enregistrement de la transaction.", "details": messages_list}, status=400)
    
    # Pour les requêtes GET, afficher le formulaire de minting
    return render (request, 'app/mint.html')


@csrf_exempt
def validate_voucher(request):
    if request.method == 'POST':
        # Récupérer les détails de la validation sous forme de JSON
        data = json.loads(request.body)
        wallet_address = data.get('walletAddress')
        voucher_id = data.get('voucherId')
        transaction_hash = data.get('transactionHash')

        success = True  # Indicateur de succès
        messages_list = []  # Liste des messages pour les retours

        try:
            # Récupérer ou créer l'utilisateur par son adresse de portefeuille
            user, created = WalletUser.objects.get_or_create(wallet_address=wallet_address)
            
            # Créer la validation
            validation = Validation.objects.create(
                user=user,
                voucher_id=voucher_id,
                transaction_hash=transaction_hash
            )
            messages_list.append(f"Validation {transaction_hash} pour le bon {voucher_id} ajoutée avec succès.")
        except Exception as e:
            success = False
            messages_list.append(f"Erreur lors de l'ajout de la validation: {str(e)}")

        # Retourne le message de succès ou d'erreur
        if success:
            return JsonResponse({"success": True, "message": "Validation enregistrée avec succès!", "details": messages_list}, status=200)
        else:
            return JsonResponse({"success": False, "message": "Erreur lors de l'enregistrement de la validation.", "details": messages_list}, status=400)
    
    # Pour les requêtes GET, afficher le formulaire de validation
    return render(request, 'app/validation.html')







