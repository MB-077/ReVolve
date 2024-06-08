from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *


router = DefaultRouter()
router.register(r'sellers', SellerViewSet)
router.register(r'seller_products', seller_productViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('sell/', create_seller_product, name='create_seller_product'),
]

