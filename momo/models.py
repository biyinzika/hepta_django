from django.db import models
from django.utils import timezone
from momoapi import *
# import httplib, urllib
# import http, urllib.request, urllib.parse, urllib.error
# import urllib, base64, http.client
# Create your models here.

class MomoRequest(models.Model):
    '''
    MomoRequest model for storing requests as request_text
    payment status to be added
    '''
    request_text = models.CharField(max_length=240)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=1, max_digits=10000)
#     payment_status = models.ForeignKey(CollectionRequest.payment_level, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.request_text


class CollectionRequest(models.Model):
    '''
    Collection request model
    Trigger a collection_request whenever a new MomoRequest object is created (foreign key as momo_request)
    Status of payment either pending or paid as in choices. (status poll)
    
    '''
#     collection request trigger
    collection_request = models.BooleanField(default=True)
    poll = models.IntegerField(default=0)
#     foreign key to momo request model
    momo_request = models.ForeignKey(MomoRequest, on_delete=models.CASCADE)
    
#     Status of payments to be updated in Momo Request
    PENDING = 'Pending'
    PAID = 'Paid'
    STATUS_CHOICES = (
        (PENDING, 'Pending'),
        (PAID, 'Paid')
    )
#     payment account type
    payment_level = models.PositiveSmallIntegerField(choices=STATUS_CHOICES, default=PENDING)
    
    def __str__(self):
        return self.poll

class Personal_Account(models.Model):
    '''
    Personal account model storing usernames as unique values
    
    '''
    name = models.CharField(max_length=200)
    username = models.CharField(unique=True, max_length=20)
    account_number = models.IntegerField(null=False)

    
    def __str__(self):
        return self.username
    
    
    def get_name(self):
        return self.username

    def delete(self):
        '''
        Account not deleted but changes is_active to False
        '''
        self.is_active = False
        self.save()
        return self
    

# class Collection(models.Model):
#     headers = {
#     # Request headers
#     'X-Reference-Id': '',
#     'Content-Type': 'application/json',
#     'Ocp-Apim-Subscription-Key': '{subscription key}',
#     }
#      
#     params = urllib.parse.urlencode({
#     })
#      
#     try:
#         conn = http.client.HTTPSConnection('ericssonbasicapi2.azure-api.net')
#         conn.request("POST", "/v1_0/apiuser?%s" % params, "{body}", headers)
#         response = conn.getresponse()
#         data = response.read()
#         print(data)
#         conn.close()
#     except Exception as e:
#         print("[Errno {0}] {1}".format(e.errno, e.strerror))
#         
# 
# class Disbursements(models.Model):
#     headers = {
#     # Request headers
#     'Authorization': '',
#     'Ocp-Apim-Subscription-Key': '{subscription key}',
#     }
#     
#     params = urllib.parse.urlencode({
#     })
#     
#     try:
#         conn = http.client.HTTPSConnection('ericssonbasicapi2.azure-api.net')
#         conn.request("POST", "/disbursement/token/?%s" % params, "{body}", headers)
#         response = conn.getresponse()
#         data = response.read()
#         print(data)
#         conn.close()
#     except Exception as e:
#         print("[Errno {0}] {1}".format(e.errno, e.strerror))
#         