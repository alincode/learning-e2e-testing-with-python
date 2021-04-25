from selenium import webdriver
import requests
from time import sleep

driver = webdriver.Chrome("./chromedriver")
driver.get("http://the-internet.herokuapp.com/broken_images")

try:
    base_url = driver.current_url
    images = driver.find_elements_by_css_selector("img")
    for img in images:
        response = requests.get(img.get_attribute('src'))
        if response.status_code != 200:
            print(img.get_attribute('outerHTML') + " is broken.")
        else:
            print(img.get_attribute('outerHTML') + " is unbroken.")
    sleep(5)
finally:
    driver.quit()