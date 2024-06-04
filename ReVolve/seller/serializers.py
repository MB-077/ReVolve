from rest_framework import serializers
from .models import *
        
class seller_productSerializer(serializers.ModelSerializer):
    class Meta:
        model = seller_product
        fields = '__all__'

class SellerSerializer(serializers.ModelSerializer):
    products = seller_productSerializer(many=True, read_only=True)

    class Meta:
        model = Seller
        fields = '__all__'