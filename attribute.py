
from selenium import webdriver
from time import sleep
import os
if 'HTTP_PROXY' in os.environ: del os.environ['HTTP_PROXY']

dr = webdriver.Chrome()
file_path = 'file:///' + os.path.abspath('attribute.html')

dr.get(file_path)

link = dr.find_element_by_id('tooltip')

sleep(1)

print(link.get_attribute('title'))

print(link.text)

dr.quit()