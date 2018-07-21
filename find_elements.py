from selenium import webdriver
import time
import os

dr=webdriver.Chrome()
file_path='file:///'+os.path.abspath('selenium-glance/checkbox.html')
dr.get(file_path)

checkboxes = dr.find_elements_by_css_selector('input[type=checkbox]')
for checkbox in checkboxes:
    checkbox.click()
time.sleep(1)
dr.refresh()
time.sleep(2)

print(len(dr.find_elements_by_css_selector('input[type=checkbox]')))

inputs=dr.find_elements_by_tag_name('input')
for input in inputs:
    if input.get_attribute('type')=='checkbox':
        input.click()

time.sleep(1)

dr.find_elements_by_css_selector('input[type=checkbox]').pop().click()
time.sleep(1)

dr.quit()