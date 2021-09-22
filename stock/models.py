from django.db import models

# Create your models here.

class Sector(models.Model):
  name = models.CharField(max_length=50)

class Market(models.Model):
  name = models.CharField(max_length=50)

class Stock(models.Model):
  sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
  market = models.ForeignKey(Market, on_delete=models.CASCADE)
  code = models.CharField(max_length=10)
  name = models.CharField(max_length=50)
  url = models.CharField(max_length=200)