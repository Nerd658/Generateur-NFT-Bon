from django.contrib import admin
from .models import WalletUser, Transaction

admin.site.register(WalletUser)
admin.site.register(Transaction)
