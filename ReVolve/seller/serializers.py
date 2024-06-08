from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
        
# class seller_productSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = seller_product
#         fields = '__all__'

class seller_productSerializer(serializers.ModelSerializer):
    seller_name = serializers.CharField(source='seller.seller_name', read_only=True)
    item_picture = serializers.ImageField(use_url=True)

    class Meta:
        model = seller_product
        fields = ['item_id', 'item_material_type', 'item_grade', 'item_condition', 'item_weight', 'item_picture', 'seller_name']

class SellerSerializer(serializers.ModelSerializer):
    products = seller_productSerializer(many=True, read_only=True)

    class Meta:
        model = Seller
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user