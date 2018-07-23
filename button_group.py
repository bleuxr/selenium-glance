from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import os

if 'HTTP_PROXY' in os.environ: del os.environ['HTTP_PROXY']

dr=webdriver.Chrome()
file_path='file:///'+os.path.abspath('button_group.html')

dr.get(file_path)
sleep(1)

buttons=dr.find_element_by_class_name('btn-group').find_elements_by_class_name('btn')
for btn in buttons:
    if btn.text == 'second': print('find second button')

sleep(2)
dr.quit()