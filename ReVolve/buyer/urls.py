from django.urls import path
from buyer.views import display_matching_seller_cards

urlpatterns = [
    path('displaysellercards/<int:buyer_need_id>/', display_matching_seller_cards, name='display_matching_seller_cards'), 
]