from django.db import models
from .profile import Profile


class Deposit(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='deposit')
    amount = models.DecimalField(max_digits=7, decimal_places=2)
    time_stamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Deposit'
        verbose_name_plural = 'Deposit'

    def __str__(self):
        return self.user.user.email + f'({self.amount})'


class Withdraw(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='withdraw')
    amount = models.DecimalField(max_digits=7, decimal_places=2)
    time_stamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Withdraw'
        verbose_name_plural = 'Withdraw'

    def __str__(self):
        return self.user.user.email + f'({self.amount})'


class Send(models.Model):
    sender = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='send')
    amount = models.DecimalField(max_digits=7, decimal_places=2)
    time_stamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Send money'
        verbose_name_plural = 'Send money'

    def __str__(self):
        return self.sender.user.email + f'({self.amount})'

