from django.dispatch import receiver
from rest_framework.decorators import action, api_view

from django.conf import settings
from django.db.models.signals import post_save

from .models import Wallet, Profile
from .serializers import WalletSerializer, UserSerializer, ProfileSerializer
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


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=False, methods=['get'])
    def get_user(self, request):
        snippets = request.user.profile.wallet
        serializer = WalletSerializer(snippets)
        return Response(serializer.data)


class ProfileViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    @action(detail=False, methods=['get'])
    def get_user(self, request):
        snippets = request.user.profile
        serializer = ProfileSerializer(snippets)
        return Response(serializer.data)


class WalletViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer

    @action(detail=False, methods=['get'])
    def get_user(self, request):
        snippets = request.user.profile.wallet
        serializer = WalletSerializer(snippets)
        return Response(serializer.data)
