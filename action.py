from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

dr=webdriver.Chrome()
dr.get('https://github.com')

element=dr.find_element_by_link_text('business')
#actions:
#key_down, key_up, click, send_keys, double_click, click_and_hold
#release, move_to_element, content_click, drag_and_drop
hov=ActionChains(dr).move_to_element(element)
hov.perform()

sleep(5)
dr.quit()