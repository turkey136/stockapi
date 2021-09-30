from django.http import HttpResponse, JsonResponse
from stock.models import Stock
from stock.serializers import StockSerializer


def index(request):
    stocks = Stock.objects.all()
    serializer = StockSerializer(stocks, many=True)
    return JsonResponse(serializer.data, safe=False)
    
