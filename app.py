from instapy import InstaPy
from selenium import webdriver

instagram_username = 'nacholesst'
instagram_password = 'caosdrc2960'

driver = webdriver.Chrome("C:/Users/Ignacio Tosolini/Downloads/chromedriver_win32/chromedriver.exe")

driver.get('https://www.instagram.com/')

driver.find_element_by_xpath("//input[@name='username']").send_keys(instagram_username)
driver.find_element_by_xpath("//input[@name='password']").send_keys(instagram_password)
driver.find_element_by_xpath("//button[@type='submit']").click()