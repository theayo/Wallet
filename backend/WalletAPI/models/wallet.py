import uuid

from django.db import models
from django.contrib.auth.models import User
from django.utils.crypto import salted_hmac


class Wallet(models.Model):
    usd = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="Usd amount")
    usd_id = models.CharField(max_length=16, verbose_name="ID for usd account", null=True)
    btc = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="Btc amount")
    btc_id = models.CharField(max_length=16, verbose_name="ID for btc account", null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='wallet',
                                verbose_name="Wallet holder")

    class Meta:
        verbose_name = 'Wallet'
        verbose_name_plural = 'Wallet'

    def fill(self):
        self.usd = 0
        self.btc = 0
        self.usd_id = Wallet.generate_account_id()
        self.btc_id = Wallet.generate_account_id()

    def __str__(self):
        return self.user.email

    @staticmethod
    def generate_account_id():
        return uuid.uuid1()
