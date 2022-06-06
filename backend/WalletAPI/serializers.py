from .models import Card, Profile, \
    Wallet, Deposit, Withdraw, Send
from rest_framework import serializers


class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ('usd', 'btc', 'usd_id', 'btc_id')
