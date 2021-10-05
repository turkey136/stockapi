from rest_framework import serializers
from stock.models import Stock, DailyStock
from datetime import datetime, timedelta


class DailyStockSerializer(serializers.ModelSerializer):
  class Meta:
        model = DailyStock
        fields = ('date', 'open', 'close', 'low', 'high', 'amount_of_change', 'rsi')

class StockListSerializer(serializers.ModelSerializer):
    market = serializers.StringRelatedField(read_only = True)
    sector = serializers.StringRelatedField(read_only = True)

    class Meta:
        model = Stock
        fields = ('code', 'name', 'market', 'sector')

class StockSerializer(serializers.ModelSerializer):
    market = serializers.StringRelatedField(read_only = True)
    sector = serializers.StringRelatedField(read_only = True)
    daily_stocks = DailyStockSerializer(read_only = True, many = True)

    class Meta:
        model = Stock
        fields = ('code', 'name', 'industry', 'url',  'market', 'sector', 'daily_stocks')
