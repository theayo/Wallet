from django.dispatch import receiver
from rest_framework.decorators import action, api_view

from django.conf import settings
from django.db.models.signals import post_save

from .models import Wallet, Profile
from .serializers import WalletSerializer, UserSerializer
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import permissions
from django.contrib.auth.models import User

from rest_framework import status, viewsets
from rest_framework.response import Response


# Create your views here.
class WalletView(generics.ListAPIView):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer


class UsersView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_wallet(sender, instance=None, created=False, **kwargs):
    if created:
        Wallet.objects.create(user=instance).fill()


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=False, methods=['get'])
    def get_user(self, request):
        snippets = request.user.wallet
        serializer = WalletSerializer(snippets)
        return Response(serializer.data)
