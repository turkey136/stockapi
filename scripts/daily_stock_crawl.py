from datetime import datetime, timedelta
from stock.models import Stock, DailyStock
import pandas_datareader.data as web

def run():
  from_date = datetime.today() - timedelta(days=2)
  target_date = [ datetime.today() - timedelta(days=1),  datetime.today() - timedelta(days=2)]
  stocks = Stock.objects.all()
  for stock in stocks:
    f = web.DataReader(sotck.code, 'stooq', from_date)
    for date in target_date:
      create_daily_stock(f[date], date, stock)

def create_daily_stock(daily_data, date, stock):
  daily_stock = DailyStock.get_or_create(stock=stock,date=date)
  daily_stock(
    close=daily_data['Close'][0],
    open=daily_data['Open'][0],
    low=daily_data['Low'][0],
    high=daily_data['High'][0],
    amount_of_change=daily_data['Close'][0] - daily_data['Open'][0]
  )
  daily_stock.save()