from selenium import webdriver
from time import sleep
import os

dr=webdriver.Chrome()
url='https://www.github.com'
dr.get(url)

print('title: %s'%(dr.title))
print('url: %s'%(dr.current_url))


sleep(2)
dr.quit()