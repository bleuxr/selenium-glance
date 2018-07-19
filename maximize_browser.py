from selenium import webdriver
import time

dr=webdriver.Chrome()
time.sleep(1)
print('maximize browser')

dr.maximize_window()
time.sleep(1)
print('close browser')

dr.quit()