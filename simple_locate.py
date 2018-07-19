from selenium import webdriver
from time import sleep
import os
if "HTTP_PROXY" in os.environ: del os.environ['HTTP_PROXY']

dr=webdriver.Chrome()
#dont know 'file:///'+ is necessary
file_path='file:///'+os.path.abspath('selenium-glance/form.html')
print(file_path)

dr.get(file_path)

dr.find_element_by_id('inputEmail').click()
sleep(1)

dr.find_element_by_name('password').click()
sleep(1)

print(dr.find_element_by_tag_name('form').get_attribute('class'))
sleep(1)

e=dr.find_element_by_class_name('controls')
dr.execute_script('$(arguments[0]).fadeOut().fadeIn()', e)
sleep(1)