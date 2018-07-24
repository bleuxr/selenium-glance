from selenium import webdriver
from time import sleep
import os
if 'HTTP_PROXY'in os.environ: del os.environ['HTTP_PROXY']

dr = webdriver.Chrome()
file_path = 'file:///' + os.path.abspath('form2.html')
dr.get(file_path)

dr.find_element_by_css_selector('input[type=checkbox]').click()
sleep(1)

dr.find_element_by_css_selector('input[type=radio]').click()
sleep(1)

dr.find_element_by_tag_name('select').find_elements_by_tag_name('option')[-1].click()
sleep(1)

dr.find_element_by_css_selector('input[type=submit]').click()
sleep(10)

alert = dr.switch_to_alert()
print(alert.text)
alert.accept()

dr.quit()