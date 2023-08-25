# import time
import time
#import webdriver
from selenium import webdriver
# to use in find_elements
from selenium.webdriver.common.by import By
# import service
from selenium.webdriver.chrome.service import Service
#import keys
from selenium.webdriver import Keys
# driver path 
path ='C:\\Users\\saifu\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe'
# define service through executable path
s=Service(executable_path=path)
#  define driver for Chrome
driver=webdriver.Chrome(service=s)

import pytest
#setup_teardown: login and logout 
@pytest.fixture()
def setup_teardown():
    # go to url
    driver.get("https://ecommerce-playground.lambdatest.io/index.php?route=account/login")
    # email 
    driver.find_element(By.ID, 'input-email')\
        .send_keys('saifur.rahman@g.bracu.ac.bd')
    # pass
    driver.find_element(By.ID, 'input-password')\
        .send_keys('darkside123')
    # click login
    driver.find_element(By.XPATH, "//input[@value='Login']")\
        .click() # make sure different quotation marks
    print('Log In')
    # return back to test function to execute test
    yield
    # click logout
    driver.find_element(By.PARTIAL_LINK_TEXT, "Logout")\
        .click() # make sure different quotation marks
    print('Log Out')
    driver.quit()
          

# test function    
def test_order(setup_teardown):
    driver.find_element(By.PARTIAL_LINK_TEXT, 'Order').click()
    
    assert driver.title == 'Order History'      
    print('Test 1 -Complete')
        
    
        
    



