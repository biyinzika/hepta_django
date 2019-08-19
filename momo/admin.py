from django.contrib import admin

# Register your models here.
from .models import MomoRequest
# from momo.models import CollectionRequest, Personal_Account

admin.site.register(MomoRequest)
# admin.site.register(CollectionRequest)
# admin.site.register(Personal_Account)