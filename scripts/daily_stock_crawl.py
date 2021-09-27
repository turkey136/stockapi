import pandas_datareader.data as web
import time
from datetime import datetime, timedelta
from stock.models import Stock, DailyStock
from multiprocessing import Pool

# dc run stockapi python3 manage.py runscript daily_stock_crawl

date_format = "%Y-%m-%d"
yesterday = (datetime.today() - timedelta(days=1)).strftime(date_format)
five_day_ago = (datetime.today() - timedelta(days=6)).strftime(date_format)

def run():
  stocks = each_slice(Stock.objects.filter(), 100)
  with Pool(processes=2) as p:
    p.map(func=create_daily_stock, iterable=stocks)

def create_daily_stock(stocks):
  try:  
    daily_data = fetch_daily_data(stocks)
    for stock in stocks:
      daily_stock = calculation_daily_stock(build_yesterday_daily_stock(stock), daily_data)
      if not daily_stock == False:
        daily_stock.save()
        print('created daily data. code: %s, date: %s' %(stock.code, yesterday))
  except Exception as e:
    for stock in stocks:
      print('error daily data. code: %s, date: %s, error: %s' %(stock.code, yesterday, e))
  finally:
    time.sleep(1)

def build_yesterday_daily_stock(stock):
  daily_stock = DailyStock.objects.filter(stock=stock,date=yesterday)
  if not daily_stock.exists():
    daily_stock = DailyStock(stock=stock,date=yesterday)
  else:
    daily_stock = daily_stock[0]
  return daily_stock

def fetch_daily_data(stocks):
  symbols =  [stock.code for stock in stocks]
  return web.DataReader(symbols, 'yahoo', five_day_ago)

def calculation_daily_stock(daily_stock, daily_data):
  stock = daily_stock.stock
  if daily_data.sum()['Open'][stock.code] == 0:
    # 過去5日にデータが無いので廃止銘柄 or 取得不可
    print('not found stock data')
    return False
  elif daily_data['Open'][stock.code][yesterday] > 0:
    daily_stock.high=daily_data['High'][stock.code][yesterday]
    daily_stock.low=daily_data['Low'][stock.code][yesterday]
    daily_stock.open=daily_data['Open'][stock.code][yesterday]
    daily_stock.close=daily_data['Close'][stock.code][yesterday]
    daily_stock.amount_of_change=daily_stock.close - daily_stock.open
  else:
    # 土日等でデータなし or 過去5日以内の廃止銘柄
    print('not found stock data')
    return False
    
  # calculation RSI
  old_stocks = DailyStock.objects.filter(stock=daily_stock.stock)[:14]
  if old_stocks.count() == 14:
    over_zeros = old_stocks.filter(amount_of_change__gte=0).aggregate(Sum('amount_of_change'))
    under_zeros = old_stocks.filter(amount_of_change__lt=0).aggregate(Sum('amount_of_change'))
    daily_stock.rsi = over_zeros / under_zeros * 100

  return daily_stock

def each_slice(arr, n):
  return [arr[i:i + n] for i in range(0, len(arr), n)]
