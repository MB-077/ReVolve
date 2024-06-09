from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

def upload_to(instance, filename):
  return 'posts/{filename}'.format(filename=filename)

class Seller(models.Model):
  seller_company_name = models.CharField(max_length=200)
  seller_username = models.CharField(max_length=200)
  seller_contact = models.CharField(max_length=14, null=True)
  seller_email = models.EmailField(max_length=200, null=True)

  def __str__(self):
    return f"{self.id} --> {self.seller_username}"
      
class seller_product(models.Model):
  item_id = models.CharField(max_length=50)
  item_material_type = models.CharField(max_length=100)
  item_grade = models.CharField(max_length=50)
  item_condition = models.CharField(max_length=400, null=True, blank=True)
  item_weight = models.FloatField(null=True, blank=True)
  item_picture = models.ImageField(_("Image"),upload_to=upload_to, null=True, blank=True)
  seller = models.ForeignKey(Seller, on_delete=models.CASCADE, related_name='products')
  
  def __str__(self):
    return f"{self.item_id} --> {self.item_material_type} from {self.seller.seller_username}"



