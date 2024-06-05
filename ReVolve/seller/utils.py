from buyer.models import buyer_need
from seller.models import seller_product

def find_matching_products(buyer_need_instance):
    # # Debugging information to verify buyer_need_instance fields
    print(f"Item Name: {buyer_need_instance.item_name}")
    print(f"Material Type: {buyer_need_instance.item_material_type}")
    print(f"Grade: {buyer_need_instance.item_grade}")
    # print(f"Volume: {buyer_need_instance.item_volume}")

    matching_products = seller_product.objects.filter(
        item_name=buyer_need_instance.item_name,
        item_material_type=buyer_need_instance.item_material_type,
        item_grade=buyer_need_instance.item_grade,
    )
    return matching_products

def get_seller_cards_for_buyer_need(buyer_need_instance):
    matching_products = find_matching_products(buyer_need_instance)
    # seller_cards = seller_product.objects.filter(product__in=matching_products)
    # return seller_cards
    return matching_products