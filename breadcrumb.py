from selenium import  webdriver
from time import sleep
import os


dr = webdriver.Chrome()
file_path = 'file:///' + os.path.abspath('breadcrumb.html')
dr.get(file_path)

anstors = dr.find_element_by_class_name('breadcrumb').find_elements_by_tag_name('a')
for ans in anstors:
    print(ans.text)

sleep(3)

print(dr.find_element_by_class_name('breadcrumb').find_element_by_class_name('active').text)

dr.quit()