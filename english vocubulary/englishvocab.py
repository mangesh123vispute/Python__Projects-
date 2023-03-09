from selenium import webdriver

# set up Microsoft Edge web driver
driver = webdriver.Edge()

# navigate to a website
driver.get('https://www.example.com/')

# find an element by its xpath
element = driver.find_element_by_xpath('//a[@href="/"]')
