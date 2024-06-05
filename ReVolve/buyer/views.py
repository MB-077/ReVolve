from django.shortcuts import render, get_object_or_404

# Create your views here.

from buyer.models import buyer_need
from seller.utils import get_seller_cards_for_buyer_need

# Pseudo-code for saving buyer needs from LLM output
def save_buyer_need_from_llm(llm_output):
    buyer_need_instance = buyer_need(
        item_name=llm_output['item_name'],
        item_material_type=llm_output['item_material_type'],
        item_grade=llm_output['item_grade'],
        item_quantity=llm_output.get('item_quantity', 1),
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



def display_matching_seller_cards(request, buyer_need_id):
    buyer_need_instance = get_object_or_404(buyer_need, id=buyer_need_id)
    # # Debugging information to verify buyer_need_instance fields
    # print(f"Buyer Need ID: {buyer_need_instance.id}")
    # print(f"Item Name: {buyer_need_instance.item_name}")
    # print(f"Material Type: {buyer_need_instance.item_material_type}")
    # print(f"Grade: {buyer_need_instance.item_grade}")
    matching_products = get_seller_cards_for_buyer_need(buyer_need_instance)
    return render(request, 'buyer/display_seller_cards.html', {'matching_products': matching_products})