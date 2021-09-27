from django.db import models
from django.utils import timezone

# Create your models here.

class Sector(models.Model):
  name = models.CharField(max_length=50, db_index=True)
  updated_at = models.DateTimeField(auto_now=True)

class Market(models.Model):
  name = models.CharField(max_length=50, db_index=True)
  updated_at = models.DateTimeField(auto_now=True)

class Stock(models.Model):
  sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
  market = models.ForeignKey(Market, on_delete=models.CASCADE)
  code = models.CharField(max_length=10, db_index=True)
  name = models.TextField(max_length=100)
  industry= models.TextField(max_length=500)
  url = models.TextField(max_length=200)
  updated_at = models.DateTimeField(auto_now=True)

class DailyStock(models.Model):
  stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
  date = models.DateField(db_index=True)
  open = models.FloatField()
  close = models.FloatField()
  low = models.FloatField()
  high = models.FloatField()
  amount_of_change = models.FloatField()
  rsi = models.FloatField(null=True)
  updated_at = models.DateTimeField(auto_now=True)

