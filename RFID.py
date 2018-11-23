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

continue_reading = True

# Capture SIGINT for cleanup when the script is aborted
def end_read(signal,frame):
    global continue_reading
    print("Ctrl+C captured, ending read.")
    continue_reading = False
    GPIO.cleanup()

def read():
    while(True):
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
            return tag

# Create an object of the class MFRC522
MIFAREReader = MFRC522.MFRC522()

chrome_options = Options()
chrome_options.add_argument("--disable-infobars")

driver = webdriver.Chrome(executable_path="/usr/lib/chromium-browser/chromedriver", chrome_options=chrome_options)
driver.fullscreen_window()

# Open initial welcome webpage
driver.get("http://localhost:5000/")

while(continue_reading):
    # Get the RFID tag when one appears
    tag = read(MIFAREReader)

    driver.get("http://localhost:5000/login?color=blue&name="+tag+"&seat=B4")

driver.close()

