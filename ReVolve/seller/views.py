from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from .models import *
from .serializers import *

class SellerViewSet(viewsets.ModelViewSet):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer

class seller_productViewSet(viewsets.ModelViewSet):
    queryset = seller_product.objects.all()
    serializer_class = seller_productSerializer

    
from django.shortcuts import render

def product_form_view(request):
    return render(request, 'seller/index.html')


