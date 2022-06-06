from django.contrib import admin
from .models import Card, Profile, \
    Wallet, Deposit, Withdraw, Send

# Register your models here.
admin.site.site_header = 'Wallet view'

admin.site.register(Card)
admin.site.register(Profile)
admin.site.register(Wallet)
admin.site.register(Deposit)
admin.site.register(Withdraw)
admin.site.register(Send)