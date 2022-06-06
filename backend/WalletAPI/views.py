from rest_framework.decorators import action, api_view

from .models import Wallet
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


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=True, methods=['get'])
    def get_user(self, request):
        holder = request.user
        resp = UserSerializer(data=holder)
        if resp.is_valid():
            return Response(resp.data)
        else:
            return Response(resp.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def snippet_list(request):
    if request.method == 'GET':
        snippets = request.user.wallet
        serializer = WalletSerializer(snippets, many=False)
        return Response(serializer.data)
