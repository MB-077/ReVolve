from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from .models import seller_product, Seller
from .serializers import *
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .serializers import seller_productSerializer, UserSerializer
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.decorators import api_view, parser_classes
from django.db import IntegrityError


class SellerViewSet(viewsets.ModelViewSet):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer

class seller_productViewSet(viewsets.ModelViewSet):
    queryset = seller_product.objects.all()
    serializer_class = seller_productSerializer


# @api_view(['POST'])
# @permission_classes([AllowAny])
# @parser_classes([MultiPartParser, FormParser])
# def create_seller_product(request):
#     seller_name = request.data.get('seller_name')
#     seller_id = Seller.objects.get(seller_name = seller_name).seller_id
#     try:
#         seller = Seller.objects.get(seller_id=seller_id)
#     except Seller.DoesNotExist:
#         return Response({'error': 'Invalid seller ID'}, status=status.HTTP_400_BAD_REQUEST)

#     data = request.data.copy()
#     data['seller'] = seller 

#     serializer = seller_productSerializer(data=data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([AllowAny])
@parser_classes([MultiPartParser, FormParser])
def create_seller_product(request):
    seller_name = request.data.get('seller')
    # print(seller_name)

    try:
        seller, created = Seller.objects.get_or_create(seller_name=seller_name)
        if seller is None:
            return Response({'error': 'Could not create or retrieve seller'}, status=status.HTTP_400_BAD_REQUEST)
    except Seller.DoesNotExist:
        return Response({'error': 'Invalid seller name'}, status=status.HTTP_400_BAD_REQUEST)

    # print(seller)
    data = request.data.copy()
    data['seller'] = seller.id  # Use seller's ID for the ForeignKey field

    serializer = seller_productSerializer(data=data)
    try:
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    except IntegrityError as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([AllowAny])
def signup_view(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        if user:
            return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    if user:
        return Response(status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    

@api_view(['GET'])
def allseller_view(request):
    try:
        products = seller_product.objects.all()  # Query the database for all seller_product instances
        serializer = seller_productSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)