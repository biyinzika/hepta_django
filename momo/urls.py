'''
Created on 10 Aug 2019

@author: benjaminsenyonyi
'''

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

]