from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated,AllowAny
from .models import Wallet
from .serializers import UserSerializer,WalletSerializer
from cards.models import Cards
from cards.serializers import CardSerializer


class RegisterViewSet(viewsets.ModelViewSet):
    queryset:''
    serializer_class = UserSerializer
    
    # Override query_set to include only the records
    # that belong to the current authenticted user
    
    # Retrieve current user's wallet
    @action(methods=['post'],detail=False,permission_classes=[AllowAny])
    def register(self, request): 
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            walletSerializer = WalletSerializer(data={"title":"My Default Wallet","owner_id":user.id})
            if walletSerializer.is_valid():
                walletSerializer.save()

            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


# User profile view set
class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = '' # Set to blank 
    serializer_class = UserSerializer
    
    # Override query_set to include only the records
    # that belong to the current authenticted user
    def get_queryset(self):
        user = User.objects.get(pk=self.request.user.id)
        return [user]
    
    # Retrieve current user's wallet
    @action(methods=['get'],detail=False,permission_classes=[IsAuthenticated])
    def wallets(self, request): 
        mywallets = Wallet.objects.filter(owner_id=request.user.id)        
        return Response([WalletSerializer(wallet).data for wallet in mywallets])
    
    

    # Retrieve current user's cards in wallet
    @action(methods=['get'],detail=False,permission_classes=[IsAuthenticated])
    def cards(self, request): 
        mywallet = Wallet.objects.get(owner_id=request.user.id)
        mycards = Cards.objects.filter(wallet_id=mywallet.id)
        
        return Response([CardSerializer(card).data for card in mycards])

    

# Authenticate user and return token
class AuthenticateUser(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })