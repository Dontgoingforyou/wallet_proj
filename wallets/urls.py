from django.urls import path

from .apps import WalletsConfig
from .views import WalletBalanceView, WalletOperationView, WalletCreateView

app_name = WalletsConfig.name

urlpatterns = [
    path('api/v1/wallets/', WalletCreateView.as_view(), name='create_wallet'),
    path('api/v1/wallets/<uuid:wallet_id>/', WalletBalanceView.as_view(), name='balance_view'),
    path('api/v1/wallets/<uuid:wallet_id>/operation/', WalletOperationView.as_view(), name='update_view'),
]