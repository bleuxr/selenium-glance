from selenium import webdriver

fd=webdriver.Chrome()
fd.implicitly_wait(10)
fd.get('http://somedomain/url_that_delays_loading')
myDynamicElement = fd.find_element_by_id("myDynamicElement")