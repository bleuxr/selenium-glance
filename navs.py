from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import os
if 'HTTP_PROXY'in os.environ: del os.environ['HTTP_PROXY']

dr = webdriver.Chrome()
file_path='file:///'+os.path.abspath('navs.html')
dr.get(file_path)
sleep(1)

dr.find_element_by_class_name('nav').find_element_by_link_text('About').click()
sleep(2)

dr.find_element_by_link_text('Home').click()
sleep(2)

dr.quit()