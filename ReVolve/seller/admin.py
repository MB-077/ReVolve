from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Seller)
admin.site.register(seller_product)
admin.site.register(seller_card)
