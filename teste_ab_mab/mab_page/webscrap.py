from random import random
from time import sleep
from selenium import webdriver

driver = webdriver.Firefox()
driver.get('http://127.0.0.1:5000/home')

PROB_TREAT, PROB_CTR = 0.42, 0.4

clicks = 100
for click in range(clicks + 1):
    btn_color = driver.find_element('name', 'yescheckbox').get_attribute('value')

    if btn_color == 'red':
        if random() < PROB_TREAT:
            driver.find_element('name', 'yescheckbox').click()
            driver.find_element('id', 'yesbtn').click()
        else:
            driver.find_element('name', 'nocheckbox').click()
            driver.find_element('id', 'nobtn').click()
    
    else:
        if random() < PROB_CTR:
            driver.find_element('name', 'yescheckbox').click()
            driver.find_element('id', 'yesbtn').click()
        else:
            driver.find_element('name', 'nocheckbox').click()
            driver.find_element('id', 'nobtn').click()
    
    sleep(0.1)