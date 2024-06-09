from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class seller_productSerializer(serializers.ModelSerializer):
    seller_username = serializers.CharField(source='seller.user.username', read_only=True)
    item_picture = serializers.ImageField(use_url=True)

    class Meta:
        model = seller_product
        fields = ['item_id', 'item_material_type', 'item_grade', 'item_condition', 'item_weight', 'item_picture', 'seller_username', 'seller']

class SellerSerializer(serializers.ModelSerializer):
    products = seller_productSerializer(many=True, read_only=True)

    class Meta:
        model = Seller
        fields = '__all__'
    
class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    contact = serializers.CharField(max_length=15, required=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'contact']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
        )
        Seller.objects.create(user=user, seller_contact=validated_data['contact'])
        return user