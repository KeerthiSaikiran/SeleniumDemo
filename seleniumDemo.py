from selenium import webdriver
import time

driver = webdriver.Edge(executable_path='C:/Program Files (x86)/msedgedriver.exe')
driver.get('https://google.com')
driver.maximize_window()

input = driver.find_element('name','q')
input.send_keys('selenium')
time.sleep(5)

button = driver.find_element('name','btnK')
button.click()

driver.back()
driver.close()
