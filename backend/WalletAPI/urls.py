from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'user', UserViewSet, basename='user')
router.register(r'profile', ProfileViewSet, basename='profile')
router.register(r'wallet', WalletViewSet, basename='wallet')
router.register(r'card', CardViewSet, basename='card')
urlpatterns = router.urls

# path('', WalletView.as_view()),
# urlpatterns = [
#     path('', UserViewSet.as_view({'get': 'get_user'})),
#     path('wallet/get_funds/{{', snippet_list),
# ]
