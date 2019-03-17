from django.db import models
from wallet.models import Wallet

class Cards(models.Model):
    title = models.CharField(max_length=255)
    value = models.DecimalField(decimal_places=2,max_digits=10)
    voucher = models.IntegerField()
    pin = models.IntegerField()
    wallet = models.ForeignKey(Wallet,related_name="wallet",on_delete=models.CASCADE,null=True)   
    description = models.TextField()
    archived = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    