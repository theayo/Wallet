from django.db import models
from .profile import Profile


class Card(models.Model):
    card_num_16 = models.CharField(max_length=16)
    card_date = models.CharField(max_length=4)
    card_holder = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='card')

    def __str__(self):
        return self.card_holder.user.email + f'({self.card_num_16[-4:]})'
