"""Module for user profile"""
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings


class Profile(models.Model):
    """Profile class(meta, output)"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    last_name = models.CharField(max_length=20, null=True)
    first_name = models.CharField(max_length=20, null=True)

    verified = models.BooleanField(default=False)

    def create(self, user):
        self.user = user
        self.last_name = 'djonny'

    def __str__(self):
        """Function for show email of object"""
        return self.user.email

    class Meta:
        """Meta class"""
        verbose_name = 'Profile'
        verbose_name_plural = 'Profile'


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_profile(sender, instance=None, created=False, **kwargs):
    if created:
        Profile.objects.create(user=instance)
