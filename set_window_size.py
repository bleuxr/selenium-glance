from selenium import webdriver
import time

dr=webdriver.Chrome()

dr.set_window_size(240,320)
dr.get('https://wwww.github.com')

time.sleep(2)
dr.quit()