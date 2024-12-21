from rest_framework.test import APITestCase
from rest_framework import status
from wallets.models import Wallet

class WalletAPITestCase(APITestCase):
    def setUp(self):
        self.wallet = Wallet.objects.create(balance=1000)
        self.wallet_url = f"/api/v1/wallets/{self.wallet.id}/"
        self.operation_url = f"/api/v1/wallets/{self.wallet.id}/operation/"

    def test_get_balance(self):
        response = self.client.get(self.wallet_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['balance'], "1000.00")

    def test_deposit(self):
        data = {"operationType": "DEPOSIT", "amount": 500}
        response = self.client.post(self.operation_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.wallet.refresh_from_db()
        self.assertEqual(float(self.wallet.balance), 1500.00)

    def test_withdraw(self):
        data = {"operationType": "WITHDRAW", "amount": 500}
        response = self.client.post(self.operation_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.wallet.refresh_from_db()
        self.assertEqual(float(self.wallet.balance), 500.00)

    def test_insufficient_funds(self):
        data = {"operationType": "WITHDRAW", "amount": 1500}
        response = self.client.post(self.operation_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)