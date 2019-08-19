from django.db import models

# Create your models here.

class ListItem(models.Model):
    list_item = models.TextField()
#     price = models.BigIntegerField()
    
    def __str__(self):
        return self.list_item
    