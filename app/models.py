from django.db import models

class Etudiant(models.Model):
    nom = models.CharField(max_length=100)
    adresse_eth = models.CharField(max_length=42)  # Adresse Ethereum doit faire 42 caractères
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom
    
    
    

from django.db import models

class WalletUser(models.Model):
    wallet_address = models.CharField(max_length=42, unique=True)

    def __str__(self):
        return self.wallet_address

class Transaction(models.Model):
    user = models.ForeignKey(WalletUser, on_delete=models.CASCADE)
    voucher_id = models.IntegerField()
    transaction_hash = models.CharField(max_length=66)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Transaction {self.transaction_hash} for voucher {self.voucher_id}"

class Validation(models.Model):
    user = models.ForeignKey(WalletUser, on_delete=models.CASCADE)
    voucher_id = models.IntegerField()
    transaction_hash = models.CharField(max_length=66)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Vallidation {self.transaction_hash} for voucher {self.voucher_id}"