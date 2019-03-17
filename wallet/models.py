from django.db import models
from django.contrib.auth.models import User

# Wallet Model.
# User -> Wallet
# User.id (PK)== Wallet.owner_id(FK)
class Wallet(models.Model):
    title = models.CharField(max_length=255)
    owner = models.ForeignKey(User,related_name="wallets",on_delete=models.CASCADE,null=True)
    created_at = models.DateTimeField(auto_now_add=True)