from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime


def get_driver(webpage):
    options = webdriver.ChromeOptions()
    options.add_argument('no-sandbox')
    options.add_argument('disable-dev-shm-usage')
    options.add_argument('disable-infobars')
    options.add_argument("start-maximized")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument('disable-blink-features=AutomationControlled')
    driver = webdriver.Chrome(options)
    driver.get(webpage)
    return driver

def get_amazon_price():
    url = "https://www.amazon.com/Coleman-Shelter-Festivals-Construction-Protection/dp/B000YEMOM4/ref=sr_1_2?crid=2ISDZMZUPFG5S&keywords=Coleman%2BGazebo%2BEvent%2BShelter%2Bfor%2BFestivals%2C&qid=1693288156&sprefix=coleman%2Bgazebo%2Bevent%2Bshelter%2Bfor%2Bfestivals%2C%2Caps%2C136&sr=8-2&th=1"
    driver = get_driver(url)
    time.sleep(2)
    title_EL = driver.find_element(by='id', value='productTitle')
    price_El = driver.find_element(by='xpath', value='//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span[2]/span[2]/span[2]')
    print(driver.title, title_EL.text, 'price:', price_El.text)
    driver.close()


if __name__ == '__main__':
    get_amazon_price()