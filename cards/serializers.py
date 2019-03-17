from rest_framework import serializers
from django.contrib.auth.models import User
from wallet.models import Wallet
from .models import Cards

# Card Serializer
class CardSerializer(serializers.ModelSerializer):
    wallet_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Cards
        fields = '__all__' # Include all fields
