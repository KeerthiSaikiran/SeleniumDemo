from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get('https://google.com')
driver.maximize_window()

page_title = driver.title

search_bar = driver.find_element('name', 'q')
user_input = 'selenium'
search_bar.send_keys(user_input)
time.sleep(5)

# # Dropdown
# selection = Select(driver.find_element(By.TAG_NAME,"MYtag"))
# 
# selection.select_by_visible_text("Apple")

button = driver.find_element(By.NAME,'btnK')
button.click()

print(page_title)

driver.back()
driver.close()
