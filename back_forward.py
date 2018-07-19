from selenium import webdriver
from time import sleep
import os

dr=webdriver.Chrome()

first_url='https://www.github.com'
print('now access %s'%(first_url))
dr.get(first_url)
sleep(1)

second_url='https://www.github.com/bleuxr'
print('now access %s'%(second_url))
dr.get(second_url)
sleep(1)

print('back to %s'%(first_url))
dr.back()
sleep(1)
print('forward to %s'%(second_url))
dr.forward()
sleep(1)
dr.quit()