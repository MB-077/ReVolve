from rest_framework import serializers
from .models import seller_product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = seller_product
        fields = '__all__'