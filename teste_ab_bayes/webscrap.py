from random import random
from selenium import webdriver

driver = webdriver.Firefox()
driver.get('http://127.0.0.1:5000/home')

clicks = 100
for click in range(clicks):
    if random() < 0.5:
        driver.find_element('name', 'yescheckbox').click()
        driver.find_element('id', 'yesbtn').click()
    else:
        driver.find_element('name', 'nocheckbox').click()
        driver.find_element('id', 'nobtn').click()