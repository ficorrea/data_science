from random import random
from time import sleep
from selenium import webdriver

driver = webdriver.Firefox()
driver.get('http://127.0.0.1:5000/home')

clicks = 50
for click in range(clicks + 1):
    if random() <= 0.3:
        driver.find_element('name', 'yescheckbox').click()
        driver.find_element('id', 'yesbtn').click()
    else:
        driver.find_element('name', 'nocheckbox').click()
        driver.find_element('id', 'nobtn').click()
    sleep(1)