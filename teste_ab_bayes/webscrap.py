import os
from random import random
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

# user_agent = 'Mozilla/5.0 (X11; Linux x86_64; rv:106.0) Gecko/20100101 Firefox/106.0'
# path_driver = '/home/felipe/Documentos/ab_bayes/geckodriver'
# path_driver = os.path.join(os.getcwd(), 'geckodriver')
# ff_service = Service(path_driver, user_agent)
# ff_options = Options()
# ff_options.set_preference('general.useragent.override', user_agent)
# driver = webdriver.Firefox(service=ff_service, options=ff_options)

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