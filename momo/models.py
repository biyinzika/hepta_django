from django.db import models
from django.utils import timezone


# Create your models here.

class MomoRequest(models.Model):
    request_text = models.CharField(max_length=240)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=1, max_digits=10000)
    payment_status = models.ForeignKey(CollectionRequest.account_type, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.request_text

class CollectionRequest(models.Model):
    
    collection_request = models.BooleanField(default=True)
    poll = models.IntegerField(default=0)
    momo_request = models.ForeignKey(MomoRequest, on_delete=models.CASCADE)
    
#     Status of payments to be updated in Momo Request
    PENDING = 'Pending'
    PAID = 'Paid'
    STATUS_CHOICES = (
        (PENDING, 'Pending'),
        (PAID, 'Paid')
    )
    account_type = models.PositiveSmallIntegerField(choices=STATUS_CHOICES, default=PENDING)
    
    def __str__(self):
        return self.poll

class Personal_Account(models.Model):
    name = models.CharField(max_length=200)
    username = models.CharField(unique=True, max_length=20)
    account_number = models.IntegerField(null=False)

    
    def __str__(self):
        return self.username
    
    
    def get_name(self):
        return self.username

    def delete(self):
        """
        Don't delete the Account
        Instead just set `is_active` to False
        """
        self.is_active = False
        self.save()
        return self
