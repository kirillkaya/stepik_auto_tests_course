from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"


try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get(link)
    price = WebDriverWait(browser,30).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )
    browser.find_element(By.ID, "book").click() 
    math_element = WebDriverWait(browser,10).until(
        EC.visibility_of_element_located((By.ID, "input_value"))
    )
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    inputValue = browser.find_element(By.ID, "answer")
    inputValue.send_keys(y)
    button = browser.find_element(By.XPATH, "//button[text()='Submit']")
    button.click()

  

finally:
    time.sleep(10)
    browser.quit