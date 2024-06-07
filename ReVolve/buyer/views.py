from django.shortcuts import render

# Create your views here.

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import buyer_need
from seller.models import seller_product
from seller.serializers import seller_productSerializer
from seller.utils import find_matching_products

# Pseudo-code for saving buyer needs from LLM output
def save_buyer_need_from_llm(llm_output):
    buyer_need_instance = buyer_need(
        item_name=llm_output['item_name'],
        item_material_type=llm_output['item_material_type'],
        item_grade=llm_output['item_grade'],
        item_quantity=llm_output.get('item_quantity'),
        item_dimension=llm_output.get('item_dimension')
    )
    buyer_need_instance.save()

# # Example usage with hypothetical LLM output
# llm_output = {
#     'item_name': 'Steel Scarp',
#     'item_material_type': 'Steel',
#     'item_grade': '304',
#     'item_quantity': 5,
#     'item_volume': 50.0
# }

# save_buyer_need_from_llm(llm_output)

@api_view(['POST'])
def get_matching_products(request):
    try:
        # Extract data from request
        data = request.data
        item_material_type = data.get('item_material_type')
        item_grade = data.get('item_grade')

        buyer_need_instance = buyer_need(
            item_material_type=item_material_type,
            item_grade=item_grade,
        )

        matching_products = find_matching_products(buyer_need_instance)
        serializer = seller_productSerializer(matching_products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)