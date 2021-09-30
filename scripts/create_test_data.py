import pandas_datareader.data as web
from datetime import datetime, timedelta
from stock.models import Stock, DailyStock, Market, Sector

# dc run stockapi python3 manage.py runscript daily_stock_crawl

date_format = "%Y-%m-%d"
from_date =  datetime.today() - timedelta(days=100)
test_code = "QQQ"

def run():
  market, _ = Market.objects.get_or_create(name="NASDAQ")
  sector, _ = Sector.objects.get_or_create(name="n/a")
  stock, _ = Stock.objects.get_or_create(code=test_code,market=market, sector=sector)
  f = web.DataReader(test_code, 'yahoo', from_date.strftime(date_format))
  for i in range(len(f.index)):
    date = f.index[i].strftime("%Y-%m-%d")
    daily_stock = DailyStock.objects.filter(stock=stock,date=date)
    if not daily_stock.exists():
      daily_stock = DailyStock(stock=stock,date=date)
    else:
      daily_stock = daily_stock[0]

    import pdb; pdb.set_trace()
    daily_stock.high=f['High'][date]
    daily_stock.low=f['Low'][date]
    daily_stock.open=f['Open'][date]
    daily_stock.close=f['Close'][date]
    daily_stock.amount_of_change=daily_stock.close - daily_stock.open

    daily_stock.save()


