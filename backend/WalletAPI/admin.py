from django.contrib import admin, auth
from .models import Card, Profile, \
    Wallet, Deposit, Withdraw, Send
from django.contrib.auth.models import User

# Register your models here.
admin.site.site_header = 'Wallet view'


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'last_login', 'is_active')
    list_filter = ('is_active', 'last_login')

    def make_active(self, request, queryset):
        rows_updated = queryset.update(is_active=True)
        if rows_updated == 1:
            message_bit = "1 user activated"
        else:
            message_bit = f"{rows_updated} user has been activated"
        self.message_user(request, f"{message_bit} successfully.")

    make_active.short_description = "Make selected users active"

    actions = [make_active]


admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(Card)
admin.site.register(Profile)
admin.site.register(Wallet)
admin.site.register(Deposit)
admin.site.register(Withdraw)
admin.site.register(Send)
