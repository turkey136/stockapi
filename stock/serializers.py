from rest_framework import serializers
from stock.models import Stock, Market, Sector

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ('code', 'name', 'industry', 'url')