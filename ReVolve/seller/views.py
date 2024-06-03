from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from .models import seller_product
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = seller_product.objects.all()
    serializer_class = ProductSerializer
    
    
from django.shortcuts import render

def product_form_view(request):
    return render(request, 'product_api_form.html')