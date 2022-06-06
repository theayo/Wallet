from .models import Card, Profile, \
    Wallet, Deposit, Withdraw, Send
from django.contrib.auth.models import User
from rest_framework import serializers


class ProfileSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('last_name', 'verified')


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerilizer(read_only=False)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'last_login', 'profile']


class WalletSerializer(serializers.ModelSerializer):

    class Meta:
        model = Wallet
        fields = ('usd', 'btc', 'usd_id', 'btc_id')
