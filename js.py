from selenium import webdriver
from time import sleep
import os
if 'HTTP_PROXY'in os.environ: del os.environ['HTTP_PROXY']

dr = webdriver.Chrome()
file_path = 'file:///' + os.path.abspath('js.html')
dr.get(file_path)

dr.execute_script('$("#tooltip").fadeOut();')
sleep(1)

button = dr.find_element_by_class_name('btn')
dr.execute_script('$(arguments[0]).fadeOut()', button)
sleep(1)

dr.quit()