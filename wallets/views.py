from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, ValidationError
from wallets.models import Wallet
from wallets.serializers import WalletSerializer
from django.db import transaction


class WalletCreateView(APIView):
    def post(self, request):
        wallet = Wallet.objects.create()
        serializer = WalletSerializer(wallet)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class WalletBalanceView(APIView):
    def get(self, request, wallet_id):
        try:
            wallet = Wallet.objects.get(id=wallet_id)
            serializer = WalletSerializer(wallet)
            return Response(serializer.data)
        except Wallet.DoesNotExist:
            raise NotFound('Кошелек не найден')


class WalletOperationView(APIView):
    def post(self, request, wallet_id):
        data = request.data
        operation_type = data.get('operationType')
        amount = data.get('amount')

        if not operation_type or not amount:
            raise ValidationError('Неверные входные данные')

        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValidationError('Сумма должна быть положительным числом')

        try:
            with transaction.atomic():
                wallet = Wallet.objects.select_for_update().get(id=wallet_id)

                if operation_type == 'DEPOSIT':
                    wallet.balance += amount
                elif operation_type == 'WITHDRAW':
                    if wallet.balance < amount:
                        raise ValidationError('Недостаточно средств')
                    wallet.balance -= amount
                else:
                    raise ValidationError('Неверные входные данные')

                wallet.save()
                serializer = WalletSerializer(wallet)
                return Response(serializer.data)
        except Wallet.DoesNotExist:
            raise NotFound('Кошелек не найден')
