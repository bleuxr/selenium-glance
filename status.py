from selenium import webdriver
from time import sleep
import os
if 'HTTP_PROXY'in os.environ: del os.environ['HTTP_PROXY']

dr = webdriver.Chrome()
file_path = 'file:///' + os.path.abspath('status.html')
dr.get(file_path)

text_field=dr.find_element_by_name('user')
print(text_field.is_enabled())

print(dr.find_element_by_class_name('btn').is_enabled())

dr.execute_script('$(arguments[0]).hide()',text_field)
print(text_field.is_displayed())
sleep(3)

radio=dr.find_element_by_name('radio')
radio.click()
print(radio.is_selected())

try:
    dr.find_element_by_id('none')
except:
    print('element does not exist')

dr.quit()