from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

dr=webdriver.Chrome()
dr.get('https://github.com')

element=dr.find_element_by_link_text('business')
hov=ActionChains(dr).move_to_element(element)
hov.perform()

sleep(5)
dr.quit()