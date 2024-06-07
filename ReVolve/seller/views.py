from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import seller_product
from .serializers import seller_productSerializer

class SellerViewSet(viewsets.ModelViewSet):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer

class seller_productViewSet(viewsets.ModelViewSet):
    queryset = seller_product.objects.all()
    serializer_class = seller_productSerializer

