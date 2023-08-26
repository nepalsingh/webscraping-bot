from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def get_driver(webpage):
  options = webdriver.ChromeOptions()
  # options.add_argument('--ignore-certificate-errors')
  # options.add_argument('--incognito')
  # options.add_argument('--headless')
  options.add_argument('no-sandbox')
  options.add_argument('disable-dev-shm-usage')
  # options.add_argument('--remote-debugging-port=9222')
  # options.add_argument('disable-gpu')
  options.add_argument('disable-infobars')
  options.add_argument("start-maximized")
  options.add_experimental_option("excludeSwitches", ["enable-automation"])
  options.add_argument('disable-blink-features=AutomationControlled')
  driver = webdriver.Chrome(options)
  driver.get(webpage)
  return driver

def clean_text(text):
  try:
    return float(text.split(": ")[1].strip())
  except Exception as e:
    return None

def main():
  driver = get_driver('https://automated.pythonanywhere.com/')
  time.sleep(2)
  element = driver.find_element('xpath','/html/body/div[1]/div/h1[2]')
  print(driver.title, clean_text(element.text))
  driver.close()

if __name__ == '__main__':
  main()