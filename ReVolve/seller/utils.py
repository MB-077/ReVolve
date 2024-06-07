from seller.models import seller_product

def find_matching_products(buyer_need_instance):
    matching_products = seller_product.objects.filter(
        item_material_type=buyer_need_instance.item_material_type,
        item_grade=buyer_need_instance.item_grade,
    )
    print("matching_products: ", matching_products)
    return matching_products