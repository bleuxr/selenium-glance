from selenium import webdriver
import time

# you need add chromedriver.exe in the Path
# or use a direct path to the chromedriver like this
# driver = webdriver.Chrome("D:/chromedriver_win32/chromedriver.exe")

dr=webdriver.Chrome()
time.sleep(1)
print('browser will be closed')
dr.quit()
#or dr.close()
print('browser is closed') 