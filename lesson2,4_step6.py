from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/cats.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element(By.ID, "button") 
  

finally:
    time.sleep(10)
    browser.quit