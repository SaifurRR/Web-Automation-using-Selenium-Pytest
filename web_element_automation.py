# to interact with website through selenium

from selenium import webdriver

from selenium.webdriver.chrome.service import Service
import pandas as pd

#website to automate:
w= 'https://www.thesun.co.uk/sport/football/'

# path of chrome driver:
path= 'C:\\Users\\saifu\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe'

# create service:
s= Service(executable_path = path) #define service

#creating driver:

driver=webdriver.Chrome(service=s)

# open driver
driver.get(w)

# Automate News: Find Elements
# 1st Extract 'Titles' & 'sub-titles' -> 

#1: go to webpage -> #2: inspect -> #3: CNTRL+F -> #4: look into <d class, which have sub-heading
#5: <div class {image, copy, article - container}

# In CNTRL+F  (type) : //div[@class="teaser-item teaser__small  theme-football"]


# title, subtitle (together):
containers = driver.find_elements(by='xpath', value='//div[@class="teaser__copy-container"]')

# title, subtitle (separately):
#1. expand 'div class'- parent -> #2.select child class corresponding to header & sub-header

titles=[]
sub_titles=[]
links=[]

# extract header separately:
for container in containers:
    title = container.find_element(by='xpath', value='./a/h2').text  #title
    subtitle = container.find_element(by='xpath', value='./a/p').text  #sub-title
    
    link = container.find_element(by='xpath', value='./a').get_attribute('href') # link is always inside 'a'-tag
    
    titles.append(title)
    sub_titles.append(subtitle)
    links.append(link)
    