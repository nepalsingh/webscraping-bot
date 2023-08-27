from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime

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
  except Exception as ef:
    return None

def get_text():
  driver = get_driver('https://automated.pythonanywhere.com/')
  time.sleep(2)
  element = driver.find_element(by='xpath',value='/html/body/div[1]/div/h1[2]')
  print(driver.title, clean_text(element.text))
  driver.close()

def write_text(text):
  filename = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
  with open(f"{filename}.txt", 'w') as f:
    f.write(str(text))

def get_auth_page():
  driver = get_driver('https://automated.pythonanywhere.com/login/')
  time.sleep(2)
  driver.find_element(by='id',value='id_username').send_keys('automated')
  driver.find_element(by='id',value='id_password').send_keys('automatedautomated' + Keys.ENTER)
  time.sleep(3)
  print(driver.current_url)
  driver.find_element(by='xpath',value='/html/body/nav/div/a').click()
  print(driver.current_url)
  time.sleep(1)
  element = driver.find_element(by='id',value='displaytimer')
  time.sleep(2)
  print(driver.title,clean_text(element.text))
  write_text(clean_text(element.text))

  driver.close()

def main():
  # get_text()

  get_auth_page()


if __name__ == '__main__':
  main()