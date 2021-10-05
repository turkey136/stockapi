from django.http import JsonResponse
from stock.models import Stock
from stock.serializers import StockSerializer, StockListSerializer

def index(request):
    stocks=Stock.objects.all()
    serializer=StockListSerializer(stocks, many=True)
    return JsonResponse(serializer.data, safe=False)

def show(request, symbol):
  stock = __exist_stock(symbol)
  if stock:
    serializer=StockSerializer(stock[0], many=False)
    return JsonResponse(serializer.data, safe=False)
  else:
    return __not_found(symbol)
 
def __not_found(symbol):
  return JsonResponse(
      status=404,
      data={ 'status':'false','message': 'not found Symbol {}'.format(symbol) }
    )

def __exist_stock(symbol):
  if len(symbol) > 0 and len(symbol) < 6:
    stock=Stock.objects.filter(code=symbol)
    if stock.exists():
      return stock

  return False