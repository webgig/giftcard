from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Wallet


# User Serializer for Users
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','email','username','password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data,*args,**kwargs):
        user = User.objects.create_user(username=validated_data['username'],
                                        password=validated_data['password'],
                                        email=validated_data['email'])
        
        return user
    
# Wallet Serializer for Wallet
class WalletSerializer(serializers.ModelSerializer):
    owner_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = Wallet
        fields = '__all__' # Include all fields

    def create(self, validated_data,*args,**kwargs):
        wallet = Wallet.objects.create(title=validated_data['title'],
                                        owner_id=validated_data['owner_id'])
        return wallet
    