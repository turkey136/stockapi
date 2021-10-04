from rest_framework import serializers
from stock.models import Stock, Market, Sector, DailyStock

class MarketSerializer(serializers.ModelSerializer):
  class Meta:
        model = Market
        fields = "__all__"

class SectorSerializer(serializers.ModelSerializer):
  class Meta:
        model = Sector
        fields = "__all__"

class DailyStockSerializer(serializers.ModelSerializer):
  class Meta:
        model = DailyStock
        fields = "__all__"

class StockListSerializer(serializers.ModelSerializer):
    market = MarketSerializer(read_only = True)
    sector = SectorSerializer(read_only = True)
    class Meta:
        model = Stock
        fields = ('code', 'name', 'market', 'sector')

class StockSerializer(serializers.ModelSerializer):
    market = MarketSerializer(read_only = True)
    sector = SectorSerializer(read_only = True)
    daily_stocks = DailyStockSerializer(read_only = True, many = True)
    class Meta:
        model = Stock
        fields = ('code', 'name', 'industry', 'url',  'market', 'sector', 'daily_stocks')
