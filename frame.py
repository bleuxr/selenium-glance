from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import os
import selenium.webdriver.support.ui as ui
if 'HTTP_PROXY'in os.environ: del os.environ['HTTP_PROXY']

dr = webdriver.Chrome()
file_path = 'file:///' + os.path.abspath('frame.html')

dr.get(file_path)

dr.switch_to_frame('f1')
dr.switch_to_frame('f2')

dr.find_element_by_id('kw').send_keys('watir-webdriver')
dr.switch_to_default_content()

dr.switch_to_frame('f1')
dr.find_element_by_link_text('click').click()

sleep(3)
dr.quit()