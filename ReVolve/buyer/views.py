from django.shortcuts import render

# Create your views here.

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import buyer_need
from seller.models import seller_product
from seller.serializers import seller_productSerializer
from seller.utils import find_matching_products
import requests


def prompt_to_data(prompt):
    post_data = {"prompt": prompt}
    try:
        response = requests.post('http://127.0.0.1:5000/tag', json=post_data)
        response.raise_for_status()
        decoded_content = response.json()
        saving_data = save_buyer_need_from_llm(decoded_content)
        return saving_data
    except requests.exceptions.RequestException as e:
        print(f"HTTP request failed: {e}")
    except ValueError as e:
        print(f"JSON decode error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}, error type: {type(e)}")
        
def save_buyer_need_from_llm(content):
    buyer_need_instance = buyer_need(
        item_material_type=content['item_material_type'],
        item_grade=content['item_grade'],
        item_quantity=content['item_quantity'],
        # item_dimension=content['item_dimension'],
        item_shape=content['item_shape'],
    )
    buyer_need_instance.save()
    return (buyer_need_instance)

@api_view(['POST'])
def get_matching_products(request):
    try:
        prompt = request.data.get('prompt')
        if prompt:
            buyer_need_instance = prompt_to_data(prompt)
        else:
            return Response({'error': 'No prompt provided'}, status=status.HTTP_400_BAD_REQUEST)
        
        item_material_type = buyer_need_instance.item_material_type
        item_grade = buyer_need_instance.item_grade
        
        buyer_need_instance = buyer_need(
            item_material_type=item_material_type,
            item_grade=item_grade,
        )

        matching_products = find_matching_products(buyer_need_instance)
        serializer = seller_productSerializer(matching_products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)