from bibliopixel.drivers.PiWS281X import PiWS281X

from led_controller.BiblioPixelLedController import BiblioPixelLedController
from lights.BestFriendLight import BestFriendLight

numLeds         = 1
driver          = PiWS281X(numLeds)
led_controller  = BiblioPixelLedController(driver)

push_button_pin = 16
colors = [(255,0,0),(0,255,0),(0,0,255),(255,255,0),(0,255,255),(255,0,255),(255,255,255),(0,0,0)]

light = BestFriendLight(led_controller, colors, push_button_pin)
light.run()
