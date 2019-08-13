from django.db import models
from django.utils import timezone

# Create your models here.

class MomoRequest(models.Model):
    request_text = models.CharField(max_length=240)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=1, max_digits=10000)
#     collection = models.BooleanField(default=True)

    def __str__(self):
        return self.request_text

class Collectionrequest(models.Model):
    momo_request = models.ForeignKey(MomoRequest, on_delete=models.CASCADE)
    collection_request = models.BooleanField(default=True)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.request_payment

class Personal_Account(models.Model):
    name = models.CharField(max_length=200)
    account_number = models.IntegerField(null=False)
    
    def __str__(self):
        return self.name, self.account_number


