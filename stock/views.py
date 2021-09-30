from django.http import JsonResponse
from stock.models import Stock
from stock.serializers import StockSerializer

def index(request):
    stocks=Stock.objects.all()
    serializer=StockSerializer(stocks, many=True)
    return JsonResponse(serializer.data, safe=False)

def show(request, symbol):
  if len(symbol) > 0 and len(symbol) < 6:
    stock=Stock.objects.filter(code=symbol)
    if stock.exists():
      serializer=StockSerializer(stock[0], many=False)
      return JsonResponse(serializer.data, safe=False)
    else:
      return not_found(symbol)
  else:
    # 不正なティッカーシンボル
    return not_found(symbol)

def not_found(symbol):
  return JsonResponse(
      status=404,
      data={ 'status':'false','message': 'not found Symbol {}'.format(symbol) }
    )