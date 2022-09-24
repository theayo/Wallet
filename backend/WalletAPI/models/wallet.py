import uuid

from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.crypto import get_random_string

from .profile import Profile


class WalletManager(models.Manager):

    def create_wallet(self, profile):
        def generate_account_id():
            return get_random_string(16)

        id_1 = generate_account_id()
        id_2 = generate_account_id()

        wallet = self.create(usd=0.00, usd_id=id_1, btc=0.00,
                             btc_id=id_2, profile=profile)
        return wallet


class Wallet(models.Model):
    usd = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="Usd amount")
    usd_id = models.CharField(max_length=16, verbose_name="ID for usd account", null=True)
    btc = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="Btc amount")
    btc_id = models.CharField(max_length=16, verbose_name="ID for btc account", null=True)
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name='wallet', null=True,
                                   verbose_name="Wallet holder")

    class Meta:
        verbose_name = 'Wallet'
        verbose_name_plural = 'Wallet'

    objects = WalletManager()

    def __str__(self):
        return self.profile.user.email

    def create(self, user):
        self.user = user
        return


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_profile(sender, instance=None, created=False, **kwargs):
    if created:
        profile = Profile.objects.get(pk=instance.profile.id)
        wallet = Wallet.objects.create_wallet(profile=profile)
        profile.wallet = wallet
