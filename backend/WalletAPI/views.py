from datetime import datetime

from rest_framework.decorators import action, api_view

from .models import Wallet, Profile, Card, Deposit, Withdraw
from .serializers import WalletSerializer, UserSerializer, ProfileSerializer, CardSerializer, WithdrawSerializer
from django.contrib.auth.models import User

from rest_framework import status, viewsets
from rest_framework.response import Response
from .serializers import Wallet

from rest_framework import permissions

from decimal import Decimal
import logging

logger = logging.getLogger(__name__)

logging.config.dictConfig({
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'console': {
            'format': '%(name)-12s %(levelname)-8s %(message)s'
        },
        'file': {
            'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'console'
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'formatter': 'file',
            'filename': 'WalletAPI/debug.log'
        }
    },
    'loggers': {
        '': {
            'level': 'DEBUG',
            'handlers': ['console', 'file']
        }
    }
})


class WithdrawViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Withdraw.objects.all()
    serializer_class = WithdrawSerializer


class CardViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Card.objects.all()
    serializer_class = CardSerializer


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=False, methods=['get'])
    def get_user(self, request):
        snippets = request.user
        serializer = UserSerializer(snippets)
        return Response(serializer.data)


class ProfileViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    @action(detail=False, methods=['get'])
    def get_user_profile(self, request):
        snippets = request.user.profile
        serializer = ProfileSerializer(snippets)
        return Response(serializer.data)


class WalletViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer

    @action(detail=False, methods=['put'])
    def withdraw(self, request):
        wallet_id = request.data.get('wallet_id')
        money_value = Decimal(request.data.get('money_value'))
        try:
            wallet_for_action = (Wallet.objects.filter(usd_id=wallet_id) | Wallet.objects.filter(btc_id=wallet_id))[0]
            if wallet_for_action.usd_id == wallet_id:
                wallet_for_action.usd = wallet_for_action.usd - money_value
                if wallet_for_action.usd < 0:
                    return Response("Not enough money")
            elif wallet_for_action.btc_id == wallet_id:
                wallet_for_action.btc = wallet_for_action.btc - money_value
                if wallet_for_action.btc < 0:
                    return Response("Not enough money")
            wallet_for_action.save()
            ser = WalletSerializer(wallet_for_action)
        except Exception:
            return Response("No such wallet id")
        print(datetime.now())
        Withdraw.objects.create(user=request.user.profile, amount=money_value, time_stamp=datetime.now())
        return Response(ser.data)

    @action(detail=False, methods=['get'])
    def get_user_wallet(self, request):
        print(request.data)
        snippets = request.user.profile.wallet
        serializer = WalletSerializer(snippets)
        return Response(serializer.data)

    @action(detail=False, methods=['put'])
    def deposit_funds(self, request):
        usd_id = request.data.get('usd_id')
        btc_id = request.data.get('btc_id')
        response = Response(status.HTTP_400_BAD_REQUEST)

        if usd_id is not None:
            try:
                usd_value = request.data.get('usd')
                wallet = Wallet.objects.filter(usd_id=usd_id)[0]
                wallet.usd = Decimal(usd_value) + wallet.usd
                wallet.save()
                response = WalletSerializer(wallet, context={'request': request})

            except Exception:
                response = Response(f"No such id wallet {usd_id}", status.HTTP_204_NO_CONTENT)

        if btc_id is not None:
            try:
                btc_value = request.data.get('btc')
                wallet = Wallet.objects.filter(btc_id=btc_id)[0]
                wallet.btc = Decimal(btc_value) + wallet.btc
                wallet.save()
                response = WalletSerializer(wallet, context={'request': request})
            except Exception:
                response = Response(f"No such id wallet {btc_id}", status.HTTP_204_NO_CONTENT)

        return Response(response.data)
