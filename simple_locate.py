from selenium import webdriver
from time import sleep
import os
if "HTTP_PROXY" in os.environ: del os.environ['HTTP_PROXY']

dr=webdriver.Chrome()
#dont know 'file:///'+ is necessary
file_path='file:///'+os.path.abspath('selenium-glance/form.html')
print(file_path)

dr.get(file_path)