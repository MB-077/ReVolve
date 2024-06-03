from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, product_form_view

router = DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('form/', product_form_view, name='product_form'),
]