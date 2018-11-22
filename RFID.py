###############################################################################
##  File:           RFID.py
##  Author:         Michael Pocta
##  Date Created:   November 21, 2018
##  Description:    This file is responsible for calling the RESTful API
##                  and handling the RFID reader.  Sends RFID tag to the 
##                  next available Service Pi through RabbitMQ and receives
##                  the user's name that corresponds to the RFID tag.


from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--disable-infobars")

driver = webdriver.Chrome(executable_path="/usr/lib/chromium-browser/chromedriver", chrome_options=chrome_options)
driver.fullscreen_window()
#driver.get("http://localhost:5000/")
#driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')
#sleep(5)

driver.get("http://localhost:5000/login?color=blue&name=Johnny&seat=B4")

sleep(10)

driver.close()
#driver = webdriver.Chrome("C:\\Users\\Michael\\Documents\\chromedriver.exe")

def read():
    # Turn on LED with saved intensity values
    print('Hello')
