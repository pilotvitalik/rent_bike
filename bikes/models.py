from django.db import models

# Create your models here.
class Bike(models.Model):
  bike_id = models.AutoField(primary_key=True)
  brand = models.CharField(max_length=100, null=False)
  rent_price = models.DecimalField(max_digits=7, decimal_places=2)
  photo = models.CharField(max_length=255)
  status_id = models.ForeignKey('rent.StatusRent', on_delete=models.SET_NULL, default='', null=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)