import pandas_datareader.data as web
import numpy as np
from datetime import datetime, timedelta
from stock.models import Stock, DailyStock, Market, Sector

# dc run --rm stockapi python3 manage.py runscript create_test_data

date_format = "%Y-%m-%d"
from_date =  datetime.today() - timedelta(days=100)
yesterday = (datetime.today() - timedelta(days=1)).strftime(date_format)
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

    daily_stock.high=f['High'][date]
    daily_stock.low=f['Low'][date]
    daily_stock.open=f['Open'][date]
    daily_stock.close=f['Close'][date]

    yesterday = (datetime.strptime(date, date_format) - timedelta(days=1)).strftime(date_format)
    day_before_yesterday_daily_stock = DailyStock.objects.filter(stock=stock,date__lte=yesterday).order_by('-date')[:1]
    if day_before_yesterday_daily_stock.exists():
      daily_stock.amount_of_change=daily_stock.close - day_before_yesterday_daily_stock[0].close

    old_stocks = DailyStock.objects.filter(stock=stock, amount_of_change__isnull=False, date__lt=date).order_by('-date')[:14]
    if old_stocks.count() == 14:
      over_zeros = np.sum([i['amount_of_change'] for i in old_stocks.values() if i['amount_of_change'] > 0])
      under_zeros = np.sum([i['amount_of_change'] for i in old_stocks.values() if i['amount_of_change'] < 0]) * -1
      daily_stock.rsi = over_zeros / (under_zeros + over_zeros) * 100

    daily_stock.save()

