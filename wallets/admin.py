from django.contrib import admin

from wallets.models import Wallet


@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
    list_display = ['id', 'balance', 'created_at', 'updated_at']