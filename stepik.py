from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

import time
import math
import os 

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
  
link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    
    # browser.execute_script("window.scrollBy(0, 100);")
    button = browser.find_element(By.CSS_SELECTOR, "button")
    button.click()
    
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    # confirm = browser.switch_to.alert
    # confirm.accept()
    
    x_element = browser.find_element(By.ID, "input_value")
    # num1 = browser.find_element(By.ID, "num1").text
    # num2 = browser.find_element(By.ID, "num2").text
    x = x_element.text
    y = calc(x)
    
    # select = Select(browser.find_element(By.TAG_NAME, "select"))
    # select.select_by_visible_text(str(y))
    
    browser.find_element(By.ID, "answer").send_keys(str(y))
    button = browser.find_element(By.CSS_SELECTOR, "button")
    button.click()
    
    # browser.find_element(By.CSS_SELECTOR, "#robotCheckbox").click()
    # browser.find_element(By.CSS_SELECTOR, "#robotsRule").click()
    """
    forms = browser.find_elements(By.CSS_SELECTOR, "input.form-control")
    for form in forms:
        form.send_keys('1')
    browser.find_element(By.ID, "file").send_keys(file_path)
        
    
    
    time.sleep(1)
    """
finally:
    time.sleep(10)
    browser.quit()