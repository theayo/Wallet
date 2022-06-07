from .models import Card, Profile, \
    Wallet, Deposit, Withdraw, Send
from django.contrib.auth.models import User
from rest_framework import serializers


class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ('usd', 'btc', 'usd_id', 'btc_id')


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ('last_name', 'first_name', 'verified')


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'last_login', 'profile']
