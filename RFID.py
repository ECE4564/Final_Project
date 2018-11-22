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

import MFRC522
import RPi.GPIO as GPIO

def read():
    # Turn on LED with saved intensity values
    print('Hello')

# Create an object of the class MFRC522
MIFAREReader = MFRC522.MFRC522()

chrome_options = Options()
chrome_options.add_argument("--disable-infobars")

driver = webdriver.Chrome(executable_path="/usr/lib/chromium-browser/chromedriver", chrome_options=chrome_options)
driver.fullscreen_window()

# Open initial welcome webpage
driver.get("http://localhost:5000/")

while(True):
#driver.get("http://localhost:5000/")
#driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')
#sleep(5)
    # Scan for cards    
    (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

    if status == MIFAREReader.MI_OK:
        print("Found Card...")

    # Get the UID of the card
    (status,uid) = MIFAREReader.MFRC522_Anticoll()

    # If a card is found
    if status == MIFAREReader.MI_OK:
        # Put RFID tag together
        tag = str(uid[0]) + '.' + str(uid[1]) + '.' + str(uid[2]) + '.' + str(uid[3])

        print("Card ID: " + tag)

        driver.get("http://localhost:5000/login?color=blue&name="+tag+"&seat=B4")

        sleep(10)

driver.close()

