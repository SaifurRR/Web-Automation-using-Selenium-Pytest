#import webdriver
import time
from selenium import webdriver
#import service
from selenium.webdriver.chrome.service import Service
#
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
#path of webdriver

path ='C:\\Users\\saifu\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe'
s= Service(executable_path = path)
#launch chromedriver
driver= webdriver.Chrome(service=s)
#link to locate
driver.get("https://www.amazon.ca/")

driver.maximize_window()

#1. locate element by id:
element=driver.find_element(by='name', value='field-keywords')#.send_keys('Selenium')#send keys: value entered in search
element.clear()
element.send_keys('Calculator')
time.sleep(5)
element.send_keys(Keys.RETURN)
time.sleep(5)


# driver.find_element(by='name', value='btnK').click()
#driver.quit()
#2. locate element by name:
#driver.find_element(by='title', value='Search').send_keys('nameaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')






