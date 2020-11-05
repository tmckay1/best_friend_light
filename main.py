import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library

from bibliopixel.drivers.PiWS281X import PiWS281X

from led_controller.BiblioPixelLedController import BiblioPixelLedController
from lights.BestFriendLight import BestFriendLight

push_button_pin = 16

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(push_button_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin to be an input pin and set initial value to be pulled low (off)

numLeds         = 1
driver          = PiWS281X(numLeds)
led_controller  = BiblioPixelLedController(driver)

colors = [(255,0,0),(0,255,0),(0,0,255),(255,255,0),(0,255,255),(255,0,255),(255,255,255),(0,0,0)]

light = BestFriendLight(led_controller, colors, push_button_pin)
light.run()
