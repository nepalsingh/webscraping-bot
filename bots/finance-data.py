import requests
from datetime import datetime
import time


def get_stock_price(stock_code,from_date,to_date):
  from_datetime = datetime.strptime(from_date,'%Y-%m-%d')
  to_datetime = datetime.strptime(to_date,'%Y-%m-%d')
  from_epoch = int(time.mktime(from_datetime.timetuple()))
  to_epoch = int(time.mktime(to_datetime.timetuple()))
  print(stock_code,from_epoch,to_epoch)
  url = f'https://query1.finance.yahoo.com/v7/finance/download/{stock_code}?period1={from_epoch}&period2={to_epoch}&interval=1d&events=history&includeAdjustedClose=true'
  headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"}

  response = requests.get(url=url,headers=headers)
  data = response.content.decode('utf-8')
  return data


def main():
  from_date = input('From date in YYYY-MM-DD format: ')
  to_date = input('To date in YYYY-MM-DD format: ')
  stock_code = input('Stock code: ')
  print(get_stock_price(stock_code,from_date,to_date))
  with open(f'{stock_code}.csv','w') as f:
    f.write(get_stock_price(stock_code,from_date,to_date))


if __name__ == '__main__':
  main()