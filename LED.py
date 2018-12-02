import RPi.GPIO as GPIO
import time
from random import randint

red = 16
green = 20
blue = 21

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.cleanup()
GPIO.setup(red,GPIO.OUT)
GPIO.setup(green,GPIO.OUT)
GPIO.setup(blue,GPIO.OUT)

class LED_random:
    def __init__(self, size, stop,color):
        self.color = color

    def flashLED(self):
        start = time.time()
            # time.time() returns the number of seconds since the unix epoch.
            # To find the time since the start of the function, we get the start
            # value, then subtract the start from all following values.
        time.clock()    
            # When you first call time.clock(), it just starts measuring
            # process time. There is no point assigning it to a variable, or
            # subtracting the first value of time.clock() from anything.
        elapsed = 0
        while elapsed < 20:
            elapsed = time.time() - start
            if self.color is "red":
                self.redBlink()
                time.sleep(1)
                self.turnOff()
            elif self.color is "green":
                self.greenBlink()
                time.sleep(1)
                self.turnOff()
            elif self.color is "blue":
                self.blueBlink()
                time.sleep(1)
                self.turnOff()


    def redBlink(self):
        # Turn off every LED
        GPIO.output(red, GPIO.LOW)
        GPIO.output(green, GPIO.LOW)
        GPIO.output(blue, GPIO.LOW)
        
        # Turn on red LED for half a second
        GPIO.output(red, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(red, GPIO.LOW)
        time.sleep(0.5)

    def greenBlink(self):
        # Turn off every LED
        GPIO.output(red, GPIO.LOW)
        GPIO.output(green, GPIO.LOW)
        GPIO.output(blue, GPIO.LOW)

        # Turn on green LED for half a second
        GPIO.output(green, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(green, GPIO.LOW)
        time.sleep(0.5)

    def blueBlink(self):
        # Turn off every LED
        GPIO.output(red, GPIO.LOW)
        GPIO.output(green, GPIO.LOW)
        GPIO.output(blue, GPIO.LOW)

        # Turn on blue LED for half a second
        GPIO.output(blue, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(blue, GPIO.LOW)
        time.sleep(0.5)

    def turnOff(self):
        # Turn off every LED
        GPIO.output(red, GPIO.LOW)
        GPIO.output(green, GPIO.LOW)
GPIO.output(blue, GPIO.LOW)