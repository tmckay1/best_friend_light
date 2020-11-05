import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library

# run the best friend light program
class BestFriendLight(object):

  # led_controller to light up the leds
  _led_controller = None

  # the colors to choose from to light up
  _colors = []

  # the current color we are on within the above color array
  _color_index = 0

  # the pin that we will use to read the push button
  _push_button_pin = 0

  # the last state of the push button pin
  _last_state = GPIO.HIGH

  def __init__(self, led_controller, colors, push_button_pin):
    super(object, self).__init__()
    self._led_controller = led_controller
    self._colors = colors
    self._push_button_pin = push_button_pin

  def run(self):
    while True:
      switched_high = GPIO.input(pin) == GPIO.HIGH and self._last_state != GPIO.HIGH
      switched_low = GPIO.input(pin) == GPIO.LOW and self._last_state != GPIO.LOW

      # as long as we did on or the other, change the color
      if switched_low or switched_high:
        switch_colors()

      self._last_state = GPIO.input(pin)

  def switch_colors(self):
    self._led_controller.turn_on_color(self._colors[self._color_index])
    self._color_index = (self._color_index + 1) % len(self._colors)