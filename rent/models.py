from django.db import models

# Create your models here.
class Rent(models.Model):
  rent_id = models.AutoField(primary_key=True)
  user = models.ForeignKey('users.User', on_delete=models.CASCADE)
  bike = models.ForeignKey('bikes.Bike', on_delete=models.CASCADE)
  start_date = models.DateTimeField()
  exp_date = models.DateTimeField()
  act_return_date = models.DateTimeField(null=True, blank=True)
  cost = models.DecimalField(max_digits=7, decimal_places=2)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

class StatusRent(models.Model):
  status_id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=50)