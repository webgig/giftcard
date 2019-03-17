from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated  # <-- Here
from rest_framework import viewsets

from cards.serializers import CardSerializer
from .models import Cards
from wallet.models import Wallet

class CardViewSet(viewsets.ModelViewSet):
    queryset = '' # Set to blank
    serializer_class = CardSerializer
    
    # Override query_set to include only the records
    # that belong to the current authenticted user
    def get_queryset(self):
        mywallet = Wallet.objects.get(owner_id=self.request.user.id)
        mycards = Cards.objects.filter(wallet_id=mywallet.id)
        return mycards
    
    # Update partial card detail
    def patch(self, request, pk):
        cardmodel = self.get_object(pk)
        serializer = CardSerializer(cardmodel, data=request.data, partial=True) # set partial=True to update a data partially
        if serializer.is_valid():
            serializer.save()
            return Response(code=201, data=serializer.data)
        return Response(code=400, data="wrong parameters")