from django.db import models

# Create your models here.

class seller_product(models.Model):
    item_id = models.CharField(max_length=50)
    item_name = models.CharField(max_length=200)
    item_material_type = models.CharField(max_length=100)
    item_grade = models.CharField(max_length=50)
    item_condition = models.CharField(max_length=400, null=True)
    item_volume = models.FloatField(null=True)
    item_cost = models.FloatField(null=True)
    
    def __str__(self):
      return f"{self.item_id} --> {self.item_name}"