from django.urls import path
from .views import get_matching_products

urlpatterns = [
    path('matching-products/', get_matching_products, name='get_matching_products'),
]