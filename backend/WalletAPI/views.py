from .models import Wallet
from .serializers import WalletSerializer
from rest_framework import generics


# Create your views here.
class WalletView(generics.ListAPIView):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer
