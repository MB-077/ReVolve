from django.db import models

# Create your models here.

class Seller(models.Model):
  seller_id = models.CharField(max_length=50, unique=True)
  seller_name = models.CharField(max_length=200)

  def __str__(self):
    return f"{self.seller_id} --> {self.seller_name}"
      
class seller_product(models.Model):
  item_id = models.CharField(max_length=50)
  item_name = models.CharField(max_length=200)
  item_material_type = models.CharField(max_length=100)
  item_grade = models.CharField(max_length=50)
  item_condition = models.CharField(max_length=400, null=True, blank=True)
  item_weight = models.FloatField(null=True, blank=True)
  item_cost = models.FloatField(null=True, blank=True)
  item_picture = models.ImageField(upload_to='seller_card_pictures', null=True, blank=True)
  seller = models.ForeignKey(Seller, on_delete=models.CASCADE, related_name='products', default=1)
  
  def __str__(self):
    return f"{self.item_id} --> {self.item_name}"
