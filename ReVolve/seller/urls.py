from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'sellers', SellerViewSet)
router.register(r'seller_products', seller_productViewSet)
router.register(r'seller_cards', seller_cardViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('form/', product_form_view, name='product_form'),
]