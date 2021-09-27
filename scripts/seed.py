import csv
import os
from stock.models import Market, Sector, Stock
# dc run stockapi python3 manage.py runscript seed

def run():
 # csv: https://nonbiri-reinvest.net/wp-content/uploads/2016/08/nyse_nasdaq_amex_stocklist_public.xlsx
  nasdaq_file_path = './scripts/seeds/nasdaq.csv'
  nyse_file_path = './scripts/seeds/nyse.csv'
  NYSE = 'NYSE'
  NASDAQ = 'NASDAQ'
  market_names = [NYSE, NASDAQ]

  for row in market_names:
    Market.objects.get_or_create(name=row)

  if os.path.exists(nasdaq_file_path):
    csv_file = csv.reader(open(nasdaq_file_path, "r"), delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
    next(csv_file)
    for row in csv_file:
      market = Market.objects.get(name=NASDAQ)
      create_stock(row, market)

  if os.path.exists(nyse_file_path):
    csv_file = csv.reader(open(nyse_file_path, "r"), delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
    next(csv_file)
    for row in csv_file:
      market = Market.objects.get(name=NYSE)
      create_stock(row, market)

def create_stock(row, market):
  sector, _ = Sector.objects.get_or_create(name=row[6])
  stock, _ = Stock.objects.get_or_create(code=row[0],market=market, sector=sector)
  stock.name=row[1]
  stock.industry=row[7]
  stock.url=row[8]
  stock.save()