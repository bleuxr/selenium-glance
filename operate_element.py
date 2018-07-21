from  selenium import webdriver
import time,os

dr=webdriver.Chrome()
file_path='file:///'+os.path.abspath('level_locate.html')
dr.get(file_path)

dr.find_element_by_link_text('Link1').click()
time.sleep(1)
dr.find_element_by_link_text('Link2').click()

element=dr.find_element_by_name('q')
element.send_keys('something')
time.sleep(1)

element.clear()
time.sleep(1)

dr.quit()