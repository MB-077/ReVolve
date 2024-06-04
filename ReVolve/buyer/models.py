from django.db import models

# Create your models here.

class buyer_need(models.Model):
    item_name = models.CharField(max_length=200)
    item_material_type = models.CharField(max_length=100)
    item_grade = models.CharField(max_length=50)
    item_quantity = models.IntegerField(default=1,null=True)
    item_dimension = models.CharField(max_length=50,null=True)

    def __str__(self):
      return f"{self.item_name}"