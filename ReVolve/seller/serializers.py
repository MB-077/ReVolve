from rest_framework import serializers
from .models import *
        
# class seller_productSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = seller_product
#         fields = '__all__'

class seller_productSerializer(serializers.ModelSerializer):
    seller_name = serializers.CharField(source='seller.seller_name', read_only=True)

    class Meta:
        model = seller_product
        fields = ['item_id', 'item_material_type', 'item_grade', 'item_condition', 'item_weight', 'item_picture', 'seller_name']

class SellerSerializer(serializers.ModelSerializer):
    products = seller_productSerializer(many=True, read_only=True)

    class Meta:
        model = Seller
        fields = '__all__'