from django.db import models
from django.contrib.auth.models import User


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

    def __str__(self):
        return self.user.email
