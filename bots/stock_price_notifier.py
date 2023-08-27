from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import datetime
import time
from send_email_ms import send_email

def set_driver(url):
  options = webdriver.ChromeOptions()
  options.add_argument('ignore-certificate-errors')
  options.add_argument('incognito')
  options.add_argument('no-sandbox')
  options.add_argument('disable-dev-shm-usage')
  options.add_argument('disable-infobars')
  options.add_argument('start-maximized')
  options.add_experimental_option('excludeSwitches', ['enable-automation'])
  options.add_argument('disable-blink-features=AutomationControlled')

  driver = webdriver.Chrome(options)
  driver.get(url)
  return driver

def get_stock_price():
    # get the stock price from the website

    url = 'https://zse.hr/en/indeks-366/365?isin=HRZB00ICBEX6'
    driver = set_driver(url)
    time.sleep(2)
    percentage = driver.find_element(by='xpath', value='//*[@id="app_indeks"]/section[1]/div/div/div[2]/span[2]').text
    return percentage

# print(get_stock_price())

if __name__ == '__main__':
    percentage_change = float(get_stock_price().split(' ')[0])
    if percentage_change < -.10:
      print('Send email')
      send_email(percentage_change)
    else:
      print('No email')