"""Module for user profile"""

from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """Profile class(meta, output)"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    verified = models.BooleanField(default=False)

    def __str__(self):
        """Function for show email of object"""
        return self.user.email

    class Meta():
        """Meta class"""
        verbose_name = 'Profile'
        verbose_name_plural = 'Profile'
